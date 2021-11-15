from odoo import models, fields, api


class WizardTesting(models.Model):
    _name = "wizard.testing"
    _description = "wizard_testing"

    name = fields.Char(string="Student Name")
    value = fields.Integer(string="Enrollment No")
    value2 = fields.Float(string="Result")

    def call_btn(self):
        print("====shfjgdshjfgdhfgdhjg")
