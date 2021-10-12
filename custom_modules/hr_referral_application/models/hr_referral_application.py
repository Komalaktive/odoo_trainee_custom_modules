from odoo import api, fields, models


class HrReferralApplication(models.Model):
    _name = "hr.referral.application"
    _description = "Practical Task"

    name = fields.Char("Name", required="True")
    email = fields.Char(string="Email")
    sequence = fields.Integer(
        "Sequence",
        default=1,
        help="Gives the sequence order when displaying a product list",
    )
    state = fields.Selection(
        string="Status",
        default="draft",
        readonly=True,
        copy=False,
        selection=[("draft", "Draft"), ("approved", "Approved"), ("cancel", "Cancel")],
    )

    currency_id = fields.Many2one("res.currency", string="Currency", copy=False)
    reference_id = fields.Many2one("hr.employee", string="Referral Name", copy=False)
    degree_id = fields.Many2one("hr.recruitment.degree", string="Degree", copy=False)
    department_id = fields.Many2one("hr.job", string="Department", copy=False)
    ex_salary = fields.Monetary(string="Expected Salary", store=True, copy=False)
    summary = fields.Text(string="Summary", copy=False)
    joining_date = fields.Date(string="Expected joining Date", copy=False)


    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('hr.referral.application') or ('New')
        return super(HrReferralApplication, self).create(vals)

    def action_approved(self):
        for rec in self:
            rec.write({"state": "approved"})

    def action_draft(self):
        for rec in self:
            rec.write({"state": "draft"})

    def action_cancel(self):
        for rec in self:
            rec.write({"state": "cancel"})
