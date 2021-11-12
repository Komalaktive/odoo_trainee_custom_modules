from datetime import date, datetime, timedelta

from odoo import api, fields, models


class PatientInfo(models.Model):
    _name = "patient.info"
    _description = "Patient Information"

    name = fields.Char(string="Name")
    problem = fields.Char(string="Problem")
    patient_email = fields.Char(string="Email")

    is_email = fields.Boolean(string="email", default=True)
    birthdate = fields.Date(string="Birthdate")

    doctor_select = fields.Many2one("res.partner", string="Doctor")

    def mail_send_action(self):
        mail_template = self.env.ref("hospital_management.email_template")
        mail_template.send_mail(self.id, force_send=True)
        # self.ensure_one()
        # ir_model_data = self.env['ir.model.data']
        # try:
        #     template_id = ir_model_data.get_object_reference('hospital_management', 'email_template')[1]
        # except ValueError:
        #     template_id = False
        # try:
        #     compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose message_wizard_form')[1]
        # except ValueError:
        #     compose_form_id = False
        # ctx = {
        #     'default_model': 'patient.info',
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id':
        #     template_id,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'force_email': True
        #     }
        # print("\n\n\nemail send\n\n\n")
        # return {
        #     'type': 'ir.actions.act_window',
        #     'View_type': 'form',
        #     'view_mode': 'form',
        #     'res_model': 'mail.compose.message',
        #     'views': [(compose_form_id, 'form')],
        #     'view_id': compose_form_id,
        #     'target': 'new',
        #     'context': ctx,
        # }

    def cron_demo_method(self):
        for rec in self:
            rec.env["patient.info"].search(
                [("birthdate", "=", fields.date.today())]
            ).mail_send_action()

    def getInvoiceData(self):
        rec = self.env["account.move"].search([])
        print("\n\n\n")
        for rec_date in rec:
            if (date.today() + timedelta(weeks=2)) == rec_date.invoice_date_due:
                print(rec_date.id, rec_date.invoice_date_due)
        print("\n\n\n")
