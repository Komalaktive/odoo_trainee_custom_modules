from odoo import fields, models
from odoo.tools.translate import _

class PurchaseOrderField(models.Model):
    _inherit = "purchase.order"

    demo_field = fields.Char(string=_("Demo Field"), default="demo")

    def _prepare_invoice(self):
        invoice_vals = super(PurchaseOrderField, self)._prepare_invoice()
        invoice_vals.update({
            'demo_field': self.demo_field
        })
        return invoice_vals
