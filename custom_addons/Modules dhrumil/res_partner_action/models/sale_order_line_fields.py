from odoo import api, fields, models
from odoo.tools.translate import _

class ResPartnerAction(models.TransientModel):
    _name = "sale.order.line.fields"
    _description = "create fields for sale order line"

    product_id = fields.Many2one('product.product', string=_("Product"))
    wizard_id = fields.Many2one('res.partner.create.record')
    quantity = fields.Float(string=_("Quantity"), default=1.0)
    product_price = fields.Float(string=_("Unit Price"))

    @api.onchange("product_id")
    def set_product_price(self):
        for rec in self:
            if rec.product_id:
                rec.product_price = rec.product_id.list_price
