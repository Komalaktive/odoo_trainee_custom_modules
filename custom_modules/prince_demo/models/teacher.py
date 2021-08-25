
from odoo import fields, models

class Teacher(models.Model):
    _name = 'teacher.teacher'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'teacher.teacher'

    name = fields.Char(string="teacher Name" )
    language = fields.Char(string="Language")
    student_id = fields.Many2one("student.student",string="Student",index=True, tracking=1)