# -*- coding: utf-8 -*-

from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = "purchase.order"

    pur_rs = fields.Char(string="Payment Details")
    suggestion = fields.Char(string="Product Suggestion")