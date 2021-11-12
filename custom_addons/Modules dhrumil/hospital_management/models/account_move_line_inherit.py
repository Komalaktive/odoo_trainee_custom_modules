from odoo import api, fields, models


class AccountMoveLineInherit(models.Model):
    _inherit = "account.move.line"

    module_creator = fields.Char(string="module creator", default="Djshah")
