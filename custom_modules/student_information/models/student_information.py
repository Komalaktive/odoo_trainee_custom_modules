from odoo import models, fields, api


class StudentInformation(models.Model):
    _name = 'student.information'
    _description = 'Student Information'

    name = fields.Char(string="Name")
    email = fields.Char(string="Email")
    mobile_number = fields.Integer(string="Mobile Number")
    country = fields.Selection(
        [("india", "india"), ("africa", "africa"), ("america","america")],
        string="Country",
        default="india",
    )
    state = fields.Selection([("gujarat","gujarat"),("rajsthan","rajsthan")],
        string = "State",)
