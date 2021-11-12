from odoo import fields, models
from odoo.tools.translate import _

class AccountMoveLineField(models.Model):
    _inherit = "account.move.line"

    made_in = fields.Char(string=_("Made In"))


    