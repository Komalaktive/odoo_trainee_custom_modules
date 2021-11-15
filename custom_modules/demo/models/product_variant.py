from odoo import api, fields, models
from odoo.tools.translate import _


class Product(models.Model):
    _inherit = "product.template"

    qty_on_order = fields.Float(string=_("Qty On Order"), default="1.0")
