from odoo import api, fields, models
from odoo.tools.translate import _

class MaxQtyAllowed(models.Model):
    _inherit = ["sale.order.line", "product.product"]

    # max_qty_allowed = fields.Float(string=_("Max. Qty Allowed"), related="product_id.qty_on_order")
    max_qty_allowed = fields.Float(string=_("Max. Qty Allowed"))

    @api.onchange("product_uom_qty")
    def qty_not_exceed(self):
        for r in self:
            if r.product_uom_qty > r.max_qty_allowed:
                self.product_uom_qty = '1.0'

    @api.onchange("max_qty_allowed")
    def max_qty_change(self):
        for r in self:
            r.max_qty_allowed = self.prduct


    