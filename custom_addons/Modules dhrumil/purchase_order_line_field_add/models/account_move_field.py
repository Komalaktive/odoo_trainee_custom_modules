from odoo import fields, models
from odoo.tools.translate import _

class AccountMoveField(models.Model):
    _inherit = "account.move"

    demo_field = fields.Char(string=_("Demo Field"))