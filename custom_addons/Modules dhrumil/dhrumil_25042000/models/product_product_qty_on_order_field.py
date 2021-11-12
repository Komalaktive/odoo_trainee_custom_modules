from odoo import fields, models
from odoo.tools.translate import _

class QtyOnOrder(models.Model):
    _inherit = "product.product"

    qty_on_order = fields.Float(string=_("Qty on order"), default=1.0, required=True)
    