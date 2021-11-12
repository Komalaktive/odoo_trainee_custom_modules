from odoo import fields, models
from odoo.tools.translate import _

class BusinessType(models.Model):
    _name = "business.type"
    _description = "Types Of Business"

    name = fields.Char(string=_("Name"), required=True) 
    active = fields.Boolean(string=_("Active"), default=True)     
        