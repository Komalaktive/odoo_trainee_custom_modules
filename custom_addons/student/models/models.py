# -*- coding: utf-8 -*-


from odoo import fields, models

class StudentProfile(models.Model):
    _name = 'stu.student'
    _description = 'student'

    name = fields.Char(string="Student Name" )
    student_id = fields.Many2one("school.profile",string="School Name",)