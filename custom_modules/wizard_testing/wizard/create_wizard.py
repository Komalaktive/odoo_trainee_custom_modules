from odoo import models, fields, api


class CreateWizard(models.TransientModel):
    _name = "create.wizard"
    _description = "Create Wizard"

    name = fields.Char(string="Name")

    def cancel_object(self):
        pass
