from odoo import api, fields, models
from odoo.tools.translate import _


class SaleLine(models.Model):
    _inherit = "sale.order.line"

    # max_on_qty = fields.Float(string=_("Max. Qty Allowed"))
    max_on_qty = fields.Float(
        string=_("Max. Qty Allowed"), compute="_compute_onchange_max_on_qty"
    )
    # related="product_id.qty_on_order",

    @api.depends("product_id")
    def _compute_onchange_max_on_qty(self):
        for r in self:
            r.max_on_qty = r.product_id.qty_on_order

    # @api.onchange('product_id')
    # def onchange_max_on_qty(self):
    #     for r in self:
    #         r.max_on_qty = r.product_id.qty_on_order


class Sale(models.Model):
    _inherit = "sale.order"

    total_capacity = fields.Float(string=_("Total Capacity"))

    def calculate_total_capacity(self):
        for order in self:
            total_capacity = 0
            for line in order.order_line:
                total_capacity += line.max_on_qty
            order.update({"total_capacity": total_capacity})
