from odoo import fields, models
from odoo.tools.translate import _

class Requirementgathering(models.Model):
    _name = "requirement.gathering"
    _description = "Requirement Gathering Model data"

    name = fields.Char(string=_("Name"), required=True)
    email = fields.Char(string=_("Email"))
    phone = fields.Integer(string=_("Phone"), required=True)
    company = fields.Char(string=_("Company"))
    business_type = fields.Many2one("business.type", string=_("Business Type"), required=True)
    category = fields.Many2one("product.public.category", string=_("Category"), required=True)
    state = fields.Selection([
        ('draft', 'draft'),
        ('won', 'won'),
        ('lost', 'lost')
    ], default='draft')   
    active = fields.Boolean(string=_("Active"), default=True) 

    def button_won_state(self):
        """ This method is button action, transfer state from draft to won """
        for rec in self:
            rec.state = 'won'

    def button_lost_state(self):
        """ This method is button action, transfer state from won to lost """
        for rec in self:
            rec.state = 'lost'