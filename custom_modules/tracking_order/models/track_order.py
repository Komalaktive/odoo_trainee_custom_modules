from odoo import api, fields, models


class TrackOrder(models.Model):
    _name = "tracking.order"
    _description = "practical Task"

    ref_id = fields.Many2one("sale.order", string="Referral Name")
    user_id = fields.Many2one("res.users", string="User Name")
