# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrderFieldAdd(models.Model):
    _inherit = "sale.order"
    
    sale_description = fields.Char(string="Sale Description")

