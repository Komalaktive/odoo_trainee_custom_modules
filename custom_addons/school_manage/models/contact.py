# -*- coding: utf-8 -*-

from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = "res.partner"

    active = fields.Boolean(string="active", default=True)
    reviews = fields.Char(string="Reviews")