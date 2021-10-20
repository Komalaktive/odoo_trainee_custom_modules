from odoo import fields, api, models


class HrEmployee(models.Model):
    _inherit = "res.partner"

    def hello_list(self):
        print("################open_view_employee_list")

        return {
            "name": "Komal",
            "type": "ir.actions.act_window",
            "view_type": "kanban",
            "view_mode": "kanban",
            "view_id": self.env.ref("hr.hr_kanban_view_employees").id,
            "res_model": "hr.employee",
        }
