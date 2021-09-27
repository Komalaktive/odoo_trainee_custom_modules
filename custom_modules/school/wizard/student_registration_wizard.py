from odoo import models, fields, api


class StudentWizard(models.TransientModel):
    _name = "student.registration.wizard"

    fees = fields.Integer(string="Registration fees")

    def cancel_object(self):
        pass
