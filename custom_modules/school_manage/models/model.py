from odoo import models, fields, api

class school_student(models.Model):
	_name = 'school_student'
	_description = 'school_student.school_student'

	name = fields.Char()
	school_id = fields.Many2one("school.profile1", string="School Name")

class SchoolProfile(models.Model):
	_name = "school.profile1"

	school_list = fields.One2many("school.student", "school_id", string="School List")