from odoo import api, fields, models


class Hejob(models.Model):
    _inherit = "hr.job"

    affordable_salary_hr = fields.Integer(string="Affordable Salary")
