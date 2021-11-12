from odoo import http
from odoo.http import request


class PatientData(http.Controller):
    @http.route("/patient", type="http", auth="public", website=True)
    def patient_details(self, **kwargs):
        patient_details = request.env["patient.info"].sudo().search([])
        return request.render(
            "hospital_management.patient_detail_template",
            {"patient_detail": patient_details},
        )
