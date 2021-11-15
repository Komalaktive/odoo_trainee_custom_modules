# -*- coding: utf-8 -*-

from odoo import api, fields, models


class DocType(models.Model):
    _name = "docu.type"
    _description = "Document Management"

    name = fields.Char(string="Name")

    def _get_default_color(self):
        return randint(1, 11)

    color = fields.Integer(string="Color Index", default=_get_default_color)
