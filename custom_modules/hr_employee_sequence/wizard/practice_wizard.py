from odoo import models, fields, _, api


class WizardPractice(models.TransientModel):
    _name = "wizard.test"
    _description = "name"
    _rec_name = "name"

    name = fields.Char()

    def test_wizard(self):
        context = self._context
        emp = self.env["hr.employee"].browse(context["active_id"])
        emp.mobile_phone = self.name
