from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError



class PurchaseRequisition(models.Model):
    _name = 'purchase.requisition'
    _inherit = 'mail.thread'
    _description = 'Purchase Requisition'
    _rec_name = 'pr_no'
    _order = 'id desc'

    pr_no = fields.Char('PR no.', default='New', copy=False, index=True)
    company_id = fields.Many2one(
        'res.company', 'Company', readonly="1",
        default=lambda self: self.env.user.company_id.id)
    created_by_id = fields.Many2one(
        'res.users', string='Created by', readonly="1",
        default=lambda self: self.env.user.id)
    approved_by_id = fields.Many2one(
        'res.users', string='Approved by', readonly="1", )
    created_date = fields.Date('Date', default=datetime.today())
    purchase_req_line_ids = fields.One2many(
        'purchase.requisition.line', 'purchase_req_id',
        string='Purchase Requisition Line Items', copy=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting for approval', 'Waiting for approval'),
        ('approved', 'Approved'),
        ('reject', 'Rejected'),
        ('closed', 'Closed'),
        ('partially approved', 'Partially Approved'),
        ('partially closed', 'Partially Closed'),
        ],
        string='Status', readonly=True, index=True, copy=False,
        default='draft', tracking=True, compute='_get_state_val', store=True)

    @api.depends('purchase_req_line_ids.pr_state')
    def _get_state_val(self):
        if self.purchase_req_line_ids and all(
                [line.pr_state == 'closed' for line in
                 self.purchase_req_line_ids]):
            self.state = 'closed'
        if self.purchase_req_line_ids and all(
                [line.pr_state == 'approved' for line in
                 self.purchase_req_line_ids]):
            self.state = 'approved'
        if self.purchase_req_line_ids and all(
                [line.pr_state == 'reject' for line in
                 self.purchase_req_line_ids]):
            self.state = 'reject'
        if self.purchase_req_line_ids and 'approved' in self.purchase_req_line_ids.mapped("pr_state") and 'waiting for approval' in self.purchase_req_line_ids.mapped("pr_state"):
            print("\n\n\n============", self.purchase_req_line_ids.mapped("pr_state"))
            self.state = 'partially approved'
        if self.purchase_req_line_ids and 'closed' in self.purchase_req_line_ids.mapped("pr_state") and 'approved' in self.purchase_req_line_ids.mapped("pr_state"):
            print("\n\n\n============", self.purchase_req_line_ids.mapped("pr_state"))
            self.state = 'partially closed'


    def _reset_sequence(self):
        for rec in self:
            current_sequence = 1
            for line in rec.purchase_req_line_ids:
                line.sequence = 'PRL0000' + str(current_sequence)
                current_sequence += 1



    @api.model_create_multi
    def create(self, values_list):
        for vals in values_list:
            if vals.get('pr_no', 'New') == 'New':
                vals['pr_no'] = self.env['ir.sequence'].next_by_code(
                    'purchase.requisition') or '/'
                vals['state'] = 'waiting for approval'
        res = super(PurchaseRequisition, self).create(values_list)
        res._reset_sequence()
        return res

    def write(self, vals):
        res = super(PurchaseRequisition, self).write(vals)
        self._reset_sequence()
        return res

    def approve_pr(self):
        for pr_line in self.purchase_req_line_ids:
            pr_line.approve_pr()

    def reject_pr(self):
        for pr_line in self.purchase_req_line_ids:
            pr_line.reject_pr()


class PurchaseRequisitionLine(models.Model):
    _name = 'purchase.requisition.line'
    _inherit = 'mail.thread'
    _description = 'Purchase Requisition Line'
    _rec_name = 'sequence'
    _order = 'id desc'

    sequence = fields.Char('PR Line Sequence', index=True)
    name = fields.Char('PR Line NO.')
    purchase_req_id = fields.Many2one(
        'purchase.requisition', string='Purchase Requisition')
    product_id = fields.Many2one('product.product', string='Product',
                                 required="1")
    product_qty = fields.Float('Qty', default="1.0")
    product_uom_id = fields.Many2one(
        'uom.uom', string='Product unit of measure',
        related='product_id.uom_id', readonly=False)
    purchase_group_id = fields.Many2one('res.users', 'Purchase group',
                                        related='product_id.categ_id.product_group_id',
                                        required="1")
    expected_delivery_date = fields.Date('Expected delivery date')
    pr_state = fields.Selection([
        ('waiting for approval', 'Waiting for approval'),
        ('approved', 'Approved'),
        ('reject', 'Rejected'),
        ('closed', 'Closed'),

        ],
        string='Status', default='waiting for approval', readonly="0")
    created_by_id = fields.Many2one('res.users', string='Created by',
                                    default=lambda self: self.env.user.id)

    def create_rfq(self):
        line_vals = []
        pr_ref = ''

        for rec in self:
            if rec.pr_state != 'approved':
                raise UserError(_(
                    'You can create rfq of the orders which are in "Approved" state.'))
            rec.write({'pr_state': 'closed'})

            pr_ref += rec.purchase_req_id.pr_no + ' , '
            print("\n\n\n=====pr_ref====", pr_ref)
            print("\n\n\n=====rec.purchase_req_id.pr_no====", rec.purchase_req_id.pr_no)
            seller = rec.product_id._select_seller(
                quantity=rec.product_qty,
                uom_id=rec.product_uom_id)
            line_vals.append((0, 0, {
                'product_id': rec.product_id.id,
                'name': rec.product_id.name,
                'product_qty': rec.product_qty,
                'product_uom': rec.product_uom_id.id,
                'date_planned': datetime.today() + relativedelta(
                    days=seller.delay if seller else 0),
            }))
        action = self.env.ref('purchase.purchase_rfq').read()[0]
        form_view = [(self.env.ref('purchase.purchase_order_form').id, 'form')]
        action['views'] = form_view
        context = {
            'default_PR_ref': pr_ref,
            'default_order_line': line_vals,
            'default_purchase_expected_delivery_date': rec.expected_delivery_date,
        }
        action['context'] = context
        return action

    def approve_pr(self):
        for pr in self:
            if pr.pr_state != 'waiting for approval':
                raise UserError(_(
                    'You can approve the orders which are in "Waiting for approval" state.'))
            pr.purchase_req_id.approved_by_id = pr.env.user.id
            pr.write({'pr_state': 'approved'})

    def reject_pr(self):
        for pr in self:
            if pr.pr_state != 'waiting for approval':
                raise UserError(_(
                    'You can reject the orders which are in "Waiting for approval" state.'))
            pr.write({'pr_state': 'reject'})

    def partially_approved(self):
        for pr in self:
            if pr.pr_state != 'Partially Approved':
                raise UserError(_(
                    'You can approve the orders which are in "partially approved" state.'))
            pr.purchase_req_id.approved_by_id = pr.env.user.id
            pr.write({'pr_state': 'approved'})

    @api.onchange('product_id')
    def onchange_product_id(self):
        if self.product_id:
            if not self.product_id.categ_id.product_group_id:
                raise UserError(
                    _(
                        'Please select product group in selected product category.'))

    @api.onchange("expected_delivery_date")
    def _compute_expected_date(self):
        if self.expected_delivery_date:
            if self.expected_delivery_date < date.today():
                raise UserError('Expected Delivery date should not be before the current date')

