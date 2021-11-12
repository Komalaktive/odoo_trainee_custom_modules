

from odoo import models, fields, api


class practical2(models.Model):
    _name = 'tracking.order'
    _description = 'practical Task'

    ref_name = fields.Many2one("sale.order", string="Ref")
    user_name = fields.Many2one("res.users", string="User Name")