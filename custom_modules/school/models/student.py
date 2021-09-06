# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Student(models.Model):
    _name = "student.student"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Student Management"

    name = fields.Char(string="Student Name")
    student_gender = fields.Selection(
        [("Female", "female"), ("Male", "male"), ("Others", "others")], string="Gender"
    )
    is_agreed = fields.Boolean(string="Is Agreed?")
    state = fields.Selection(
        string="Status",
        default="draft",
        readonly=True,
        copy=False,
        selection=[("draft", "Draft"), ("confirm", "Validated"), ("done", "Done")],
    )
    roll_no = fields.Integer(string="Roll No")
    address = fields.Char(string="Address")
    color = fields.Integer()
    teacher_ids = fields.One2many(
        "teacher.teacher", "student_id", string="teacher", index=True, tracking=1
    )
    field_with_url = fields.Char("URL", default="www.odoo.com")

    def action_confirm(self):
        self.state = "confirm"

    def action_draft(self):
        self.state = "draft"

    def action_done(self):
        self.state = "done"

    @api.model
    def name_create(self, name):
        print("Self", self)
        print("Student Name", name)
        rtn = self.create({"name": name})
        print("\n\nrtn", rtn)
        print("rtn.name_get()[0]", rtn.name_get()[0])
        return rtn.name_get()[0]

    @api.model
    def default_get(self, fields_list=[]):
        print("\n\n\n\nfields_list", fields_list)
        rtn = super(Student, self).default_get(fields_list)
        print("beforeeeeeeeeee", rtn)
        rtn.update({"address": "abcccccc......"})
        rtn.update({"roll_no": "12"})
        print("\n\n\nReturn statement", rtn)
        # rtn['is_agreed'] = True
        return rtn

    def unlink(self):
        rtn = super(Student, self).unlink()
        return rtn

    def clear_record_data(self):
        self.write(
            {
                "name": "",
                "student_gender": "",
                "is_agreed": "",
                "roll_no": "",
                "address": "",
            }
        )

    @api.returns("self", lambda value: value.id)
    def copy(self, default={}):
        # default['active'] = False
        default["name"] = "copy (" + self.name + ")"
        print("default values", default)
        # print("self recordset ",self)
        rtn = super(Student, self).copy(default=default)
        print("Return statement", rtn)
        return rtn

    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    #     print("view id",view_id)
    #     print("view Type ",view_type)
    #     print("toolbar",toolbar)
    #     print("submenu",submenu)
    #     res = super(Student, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
    #     print("Return Disc",res)
    #     return res
