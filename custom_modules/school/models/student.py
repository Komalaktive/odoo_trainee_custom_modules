# -*- coding: utf-8 -*-

from odoo import fields, models


class Student(models.Model):
    _name = "student.student"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Student Management"

    name = fields.Char(string="Student Name")
    student_gender = fields.Selection(
        [("Female", "female"), ("Male", "male"), ("Others", "others")],
        string="Gender"
    )
    is_agreed = fields.Boolean(string="Is Agreed?")
    roll_no = fields.Integer(string="Roll No")
    address = fields.Char(string="Address")
    color = fields.Integer()
    teacher_ids = fields.One2many(
        "teacher.teacher", "student_id", string="teacher", index=True, tracking=1
    )
    field_with_url = fields.Char('URL', default='www.dhruvish09.com')