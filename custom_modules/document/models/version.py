# -*- coding: utf-8 -*-

from odoo import api, fields, models


class DocVersion(models.Model):
    _name = "docu.version"
    _description = "Document version"
    _rac_name = "version"

    name = fields.Integer(string="version")
    active = fields.Boolean(string="active", default="True")
