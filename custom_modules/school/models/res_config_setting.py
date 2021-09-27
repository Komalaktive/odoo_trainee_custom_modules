from odoo import api, fields, models
from ast import literal_eval
from datetime import date, datetime



class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def _domain_partner_id(self):
        print("======self domain partner0=====",self)
        # partners = self.env['sale.order'].search([]).filtered(lambda l: l.date_order.month == datetime.today().month).mapped("partner_id")
        # print("===partners==", partners, len(partners))
        # if not self.user_has_groups('hr_timesheet.group_hr_timesheet_approver'):
        #   return [('user_id', '=', self.env.user.id)]
        # return [('partner_id', 'in', partners)]

    module_sale_management = fields.Boolean("Sales")
    # group_sale_delivery_address = fields.Boolean("Customer Addresses",
    #                   implied_group='sale.group_delivery_invoice_address')
    teacher_active = fields.Boolean('Teacher Active Boolean', config_parameter='school.teacher_active')
    teacher_active_name = fields.Char('Teacher Active Name',config_parameter='school.teacher_name')
    primary_school = fields.Char('Primary School')
    partner_ids = fields.Many2many('res.partner','partner_schhol_rel','school_id','partner_id',string="Partners")
    # partner_ids = fields.Many2many('res.partner','partner_schhol_rel','school_id','partner_id',string="Partners", domain=_domain_partner_id)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['primary_school'] = self.env['ir.config_parameter'].get_param('school.primary_school')

        # partners = self.env['sale.order'].search([]).filtered(
        #   lambda l: l.date_order.month == datetime.today().month).mapped("partner_id")
        # print("===get partners==", partners, len(partners))

        partner_ids= self.env['ir.config_parameter'].get_param('school.partner_ids')
        print("===get==",partner_ids)
        res.update(
            partner_ids = [(6,0,literal_eval(partner_ids))],
        )
        return res

    def set_values(self):
        self.env['ir.config_parameter'].set_param('school.primary_school', self.primary_school)

        print("====set===",self.partner_ids)
        partners = self.env['sale.order'].search([]).filtered(lambda l: l.date_order.month == datetime.today().month).mapped("partner_id")
        print("\n\n\n\n\n\n\n\n==set =partners==",partners, len(partners))
        print("\n\n\n\n\n\n\n\n==set =partners==",partners.ids, len(partners))

        # self.env['ir.config_parameter'].set_param('school.partner_ids',partners.ids)
        # self.env['ir.config_parameter'].set_param('school.partner_ids',self.partner_ids.ids)
        return super(ResConfigSettings, self).set_values()



