from random import randint

from odoo import api, fields, models


class DocumentTags(models.Model):
    _name = "docu.tags"
    _description = "Documentation of tag's"
    _rec_name = "tag"

    tag = fields.Char(string="Tag", required=True)
    active = fields.Boolean(string="Active", default=True)

    def _get_default_color(self):
        return randint(1, 11)

    color = fields.Integer(string="Color Index", default=_get_default_color)
