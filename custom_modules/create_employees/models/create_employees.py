from datetime import date

from odoo import api, fields, models
from odoo.exceptions import UserError


class CustomerDocument(models.Model):
    _name = "create.employees"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = " This module is used for create Employees"

    name = fields.Char(string="Name", required=True)
    birth_date = fields.Date(string="Birth Date")
    age = fields.Char("Age", readonly="1")
    street = fields.Char(string="Street")
    state_id = fields.Many2one("res.country.state", string="State")
    country_id = fields.Many2one("res.country", string="Country")
    city = fields.Char(string="City")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    gender = fields.Selection(
        string="Gender", selection=[("male", "Male"), ("female", "Female")]
    )
    state = fields.Selection(
        string="Status",
        default="draft",
        readonly=True,
        copy=False,
        selection=[("draft", "Draft"), ("approved", "Approved"), ("cancel", "Cancel")],
    )
    experience_info = fields.Text(string="Experience Info")
    expected_salary = fields.Integer(string="Expected Salary")
    job_position_id = fields.Many2one("hr.job", string="Job Position")
    affordable_salary = fields.Integer(
        related="job_position_id.affordable_salary_hr",
        string="Affordable Salary",
        readonly="1",
    )
    extra_amount = fields.Float(string="Extra Amount")
    yearly_amount = fields.Float(string="Yearly Amount")
    monthly_amount = fields.Float(string="Monthly Amount")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    def action_approved(self):
        for rec in self:
            rec.write({"state": "approved"})

    def action_draft(self):
        for rec in self:
            rec.write({"state": "draft"})

    def action_cancel(self):
        for rec in self:
            rec.write({"state": "cancel"})

    # calculate_age function
    def calculate_age(self):
        for record in self:
            if record.birth_date:
                age = date.today().year - record.birth_date.year
                record.age = str(age) + " years"
                if age < 18:
                    raise UserError("The Employee age cannot be less than 18 years")
            else:
                raise UserError("Please select birth date than calculate age.")
