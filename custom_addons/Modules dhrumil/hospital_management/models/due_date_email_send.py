from datetime import date, datetime, timedelta

from odoo import api, fields, models


class DueDateMailSend(models.Model):
    _inherit = "account.move"

    def mail_send_action(self):
        mail_template = self.env.ref("hospital_management.account_move_email_template")
        mail_template.send_mail(self.id, force_send=True)

    def email_cron_method(self):
        recr = self.env["account.move"].search([])
        print("\n\n\n")
        for rec_date in recr:
            if rec_date.invoice_date_due and (
                (date.today() + timedelta(weeks=2)) == rec_date.invoice_date_due
            ):
                print(rec_date.id, rec_date.invoice_date_due)
                rec_date.mail_send_action()
        print("\n\n\n")
