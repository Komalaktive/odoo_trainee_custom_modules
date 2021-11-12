from odoo import api, fields, models


class DocumentVersion(models.Model):
    _name = "docu.version"
    _description = "Documentation version"
    _rec_name = "version"

    version = fields.Integer(string="Version", required=True)
    active = fields.Boolean(string="Active", default=True)

