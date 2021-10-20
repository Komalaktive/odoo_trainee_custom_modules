from datetime import date

from odoo import api, fields, models
from odoo.exceptions import UserError


class CustomerDocument(models.Model):
    _name = "customer.document"
    _description = "This is customer document form"
    _rec_name = "name"

    name = fields.Char(string="Name")
    birth_date = fields.Date(string="Birth Date")
    expiry_date = fields.Date(string="Expiry Date")
    age = fields.Integer(string="Age", readonly="1")
    customer_name_id = fields.Many2one("res.partner", string="Customer Name")
    state = fields.Selection(
        string="Status",
        default="draft",
        readonly=True,
        copy=False,
        selection=[
            ("draft", "Draft"),
            ("approved", "Approved"),
            ("expired", "Expired"),
            ("refused", "Refused"),
        ],
    )

    @api.onchange("expiry_date")
    def _compute_date(self):
        if self.expiry_date == date.today():
            self.write({"state": "expired"})

    @api.depends("age")
    def _compute_age(self):
        today = date.today()
        age = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )

    # calculate age
    # def calculate_age(self):
    #     for record in self:
    #         if record.birth_date:
    #             age = date.today().year - record.birth_date.year
    #             record.age = str(age) + " years"
    #             if age < 18:
    #                 raise UserError("The customer age can not be below 18 ")
    #             else:
    #                 raise UserError("Please select the date of birth ")
