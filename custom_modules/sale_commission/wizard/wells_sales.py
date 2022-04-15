from odoo import models, fields, api
from datetime import date, datetime

class WellsSalesWizard(models.TransientModel):
    _name = "wells.sales.wizard"
    _description = "Wells Sales Wizard"

    from_date = fields.Date(string="From Date")
    to_date = fields.Date(string="To Date")
    customer_selection = fields.Selection([('all_customer', 'All Customers'), ('specific_customer', 'Specific Customers')], string='Customer Selection', default="all_customer")
    partner_ids = fields.Many2many('res.partner', string="Customers")


    def print_wells_sales_report(self):
        return self.env.ref('sale_commission.action_wells_sales_html_report').report_action(self.ids)


    def get_sale_order(self):
        sale_env = self.env['sale.order'].sudo()
        
        sale_domain = []
        
        sale_domain.append(('state', 'in', ['sale', 'done']))
        if self.from_date:
            sale_domain.append(('date_order', '>=', self.from_date))
        if self.to_date:
            sale_domain.append(('date_order', '<=', self.to_date))
        if self.partner_ids:
            sale_domain.append(('partner_id', "in", self.partner_ids.ids))

        sale_records = sale_env.search(sale_domain)

        partner_recs = sale_records.mapped('partner_id')
        sale_records = sale_env.search(sale_domain)


        partner_dict = {}
        for partner_rec in partner_recs:
            partner_dict[partner_rec] = sale_records.search([('partner_id', '=', partner_rec.id)])
        print("\n\n partner_dict", partner_dict)
        return partner_dict

