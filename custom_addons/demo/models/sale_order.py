from odoo import api, fields, models
from odoo.tools.translate import _


class SaleLine(models.Model):
    _inherit = "sale.order.line"

    product_id = fields.Many2one("product.product")
    max_on_qty = fields.Float(
        related="product_id.qty_on_order", string=_("Max. Qty Allowed")
    )
   

class Sale(models.Model):
    _inherit = "sale.order"

    total_capacity = fields.Float(string=_("Total Capacity"))

    def calculate_total_capacity(self):
        for order in self:
            total_capacity = 0
            for line in order.order_line:
                total_capacity += line.max_on_qty
            order.update({"total_capacity": total_capacity})


