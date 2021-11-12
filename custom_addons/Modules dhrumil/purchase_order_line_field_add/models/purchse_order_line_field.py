from odoo import fields, models
from odoo.tools.translate import _

class PurchaseOrderLineField(models.Model):
    _inherit = "purchase.order.line"

    made_in = fields.Char(string=_("Made In"), default="India")

    def _prepare_account_move_line(self, move=False):
        res = super(PurchaseOrderLineField, self)._prepare_account_move_line()
        res.update({
            'made_in': self.made_in,
        })    
        return res