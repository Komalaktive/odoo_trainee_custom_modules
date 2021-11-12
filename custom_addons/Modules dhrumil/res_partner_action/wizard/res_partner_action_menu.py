from odoo import api, fields, models
from odoo.tools.translate import _

class ResPartnerAction(models.TransientModel):
    _name = "res.partner.create.record"
    _description = "create res.partner record by action menu"

    date = fields.Date(string=_("Date"))

    sale_order_lines_ids = fields.One2many("sale.order.line.fields", "wizard_id", string=_("Order_lines"))

    def close_wizard(self):
        active_ids = self.env.context.get('active_ids', [])
        print("\n\n\nactiveids\n\n\n", active_ids)

        res = self.env['res.partner.create.record'].search([])
        print("\n\n\nres\n\n\n", res)

        for sale_records in res:
            print("\n\n\ndate\n\n\n", sale_records.date)
            print("\n\n\nlines\n\n\n", sale_records.sale_order_lines_ids)

        # for r in res:
        #     print("\n\nr\n\n", r.date, r.sale_order_lines_ids, r.sale_order_lines_ids.product_id)
        # print("\n\n\nres\n\n\n", res)
        return {
            "type": "ir.actions.act_window",
            "name": "SaleOrder",
            "view_mode": "tree,form",
            "res_model": "sale.order",
        }
        
