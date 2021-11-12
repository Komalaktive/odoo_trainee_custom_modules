from odoo import api, fields, models


class AccountMoveInherit(models.Model):
    _inherit = "account.move"

    field_created_by = fields.Char(string="created_by")
