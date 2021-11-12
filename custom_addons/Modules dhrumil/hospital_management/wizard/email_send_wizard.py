from odoo import api, fields, models


class EmailSendWizard(models.TransientModel):
    _name = "email.send.wizard"
    _description = "email send using wizard"

    is_email = fields.Boolean(string="email", default=True)

    def send_mail(self):
        print("\n\n\nself\n\n\n", self)
        mail_template = self.env.ref("hospital_management.email_template")
        mail_template.send_mail(self.id, force_send=True)
