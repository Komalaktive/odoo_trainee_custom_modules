from odoo import api, fields, models


class Practical(models.Model):
	_name = "hr.referral.application"
	_description = "Practical Task"

	name = fields.Char(string="Name")
	email = fields.Char(string="Email")
	state = fields.Selection(
        string="Status",
        default="draft",
        readonly=True,
        copy=False,
        selection=[("draft", "Draft"), ("approved", "Approved"), ("cancel", "Cancel")],
    )

	ref_name = fields.Many2one("hr.employee", string="Referral Name")
	degree = fields.Many2one("hr.recruitment.degree", string="Degree")
	dept = fields.Many2one("hr.job", string="Department")
	ex_salary = fields.Integer(string="Expected Salary")
	summary = fields.Text(string="Summary")
	joining_date = fields.Date(string="Expected joining Date")
	
	def action_approved(self):
		self.state = "approved"
	 



	def action_draft(self):
		self.state = "draft"

	def action_cancel(self):
		 self.state = "cancel"
