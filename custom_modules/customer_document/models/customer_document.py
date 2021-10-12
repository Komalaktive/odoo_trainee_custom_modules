from odoo import models, fields, api
from datetime import date


class CustomerDocument(models.Model):
    _name = 'customer.document'
    _description = 'This is customer document form'

    name = fields.Char(string="Name")
    birth_date = fields.Date(string="Birth Date")
    expiry_date = fields.Date(string="Expiry Date")
    age = fields.Integer(string="Age")
    customer_name = fields.Many2one("res.partner", string="Customer Name")
    state = fields.Selection(
        string="Status",
        default="draft",
        readonly=True,
        copy=False,
        selection=[("draft", "Draft"), ("approved", "Approved"), ("expired", "Expired"), ("refused", "Refused")],
    )

    @api.depends('age')
    def _compute_age(self):
        today = date.today()
        age = today.year - birth_date.year -((today.month, today.day) < (birth_date.month, birth_date.day))

    def calculate_age(self):
        for record in self:
            if record.birth_date:
                age = date.today().year - record.birth_date.year
                record.age = str(age) + " years"
                if age < 18:
                    raise UserError( "The customer age is below 18")