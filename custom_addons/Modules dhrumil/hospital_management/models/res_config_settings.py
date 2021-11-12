from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    patient_name = fields.Many2one(
        "patient.info",
        string="Name",
        config_parameter="hospital_management.patient_name",
    )
    patient_case = fields.Selection(
        [("is_old_case", "Old Case"), ("is_new_case", "New Case")],
        default="is_new_case",
        config_parameter="hospital_management.patient_case",
    )
    case_fee = fields.Boolean(
        string="Case Fee", config_parameter="hospital_management.case_fee"
    )

    @api.model
    def set_values(self):
        self.env["ir.config_parameter"].sudo().set_param(
            "hospital_management.patient_case", self.patient_case
        )

        super(ResConfigSettings, self).set_values()

    # def set_values(self):
    #     super(ResConfigSettings, self).set_values()
    #     self.env['ir.config_parameter'].sudo().set_param('hospital_management.patient_case', self.patient_case)
    #     pt = self.env.ref('hospital_management.patient_case', True)
    #     print("\n\npt\n\n", pt)
    # if self.patient_case == 'is_new_case':
    #     self.env['ir.config_parameter'].set_param('hospital_management.case_fee', False)

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()
    #     print("\n\n\nres\n\n\n", res)
    #     return res
