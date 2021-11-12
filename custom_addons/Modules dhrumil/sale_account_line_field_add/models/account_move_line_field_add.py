from odoo import api, fields, models


class AccountMoveLineFieldAdd(models.Model):
    _inherit = "account.move.line"

    address = fields.Char(string="Address")
