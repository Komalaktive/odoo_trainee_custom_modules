# -*- coding: utf-8 -*-

from odoo import fields, models

class Student(models.Model):
    _name = 'student.student'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Student Management'

    name = fields.Char(string="Student Name" )
    roll_no = fields.Integer(string="Roll No")
    address =fields.Char(string="Address")
    teacher_ids = fields.One2many('teacher.teacher','student_id',string="teacher",index=True, tracking=1)