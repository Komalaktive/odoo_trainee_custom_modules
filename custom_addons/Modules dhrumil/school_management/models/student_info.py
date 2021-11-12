import datetime

from odoo import api, fields, models


class ResPartnerInherit(models.Model):
    _inherit = "res.partner"

    isstudent = fields.Boolean(string="isStudent", default=True)
    school_name = fields.Char(string="School Name")
    field_creator_name = fields.Char(string="Field Creator name")
    field_creator_surname = fields.Char(string="Field Creator surname")

    def Smart_button_click(self):
        print("\n\n\n\nsmart button click event occur\n\n\n\n")
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Purchase",
            "view_mode": "tree,form",
            "res_model": "purchase.order",
            # 'domain': [('driver_id', '=', self.id)],
            "domain": []
            # 'context': "{'create': False}"
        }


class StudentInfo(models.Model):
    _name = "student.info"
    _inherit = ["portal.mixin", "mail.thread"]
    _description = "Student Information"
    _order = "id desc"

    def _compute_access_url(self):
        super(StudentInfo, self)._compute_access_url()
        for stu in self:
            stu.access_url = "/student/data/%s" % (stu.id)

    name = fields.Char(string="Name", required=True)
    birthdate = fields.Date(string="Birthdate")
    age = fields.Char(string="Age", compute="get_student_age", store=True)
    student = fields.Boolean(string="Student")
    roll_number = fields.Integer(string="Rollnumber", required=True)
    email = fields.Char(string="Email", size=45)
    contact_number = fields.Char(string="Contact Number")
    address = fields.Text(string="Address")
    height = fields.Float(string="Height")
    aadhar_card = fields.Binary(string="Aadhar Card")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("others", "Others")], string="Gender"
    )
    newdate = fields.Datetime()
    student_note = fields.Text(string="Student Note")
    teacher_note = fields.Text(string="Teacher Note")
    attendence = fields.Float(string="Attendence(%)")
    standard = fields.Selection(
        [
            ("5", "5"),
            ("6", "6"),
            ("7", "7"),
            ("8", "8"),
            ("9", "9"),
            ("10", "10"),
            ("11", "11"),
            ("12", "12"),
        ],
        string="Standard", tracking=True
    )
    user_id = fields.Many2one("res.users", default=lambda self: self.env.user)
    color = fields.Integer(string="Color Index", default=0)
    internal_mark = fields.Float(string="Internal")
    final_mark = fields.Float(string="Final")
    blood_group = fields.Char(string="Blood Group")
    image = fields.Binary(string="Student Image", attachment=True)
    teacher_id = fields.Many2one("teacher.info", string="Teacher")
    teacher_subject = fields.Char(string="Teacher Subject")
    sport_ids = fields.Many2many(
        "sport.info", "student_sports_relation", "student_id", "sports_id"
    )
    category_id = fields.Many2many("res.partner.category", string="Category")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("confirm", "Confirm"),
            ("cancel", "Cancel"),
            ("done", "Done"),
        ],
        string="Status",
        default="draft",
    )
    school_medium = fields.Selection(
        [
            ("primary", "Primary"),
            ("secondary", "Secondary"),
            ("higher_secondary", "Higher Secondary"),
        ],
        string="Medium",
        compute="set_student_medium",
    )
    active = fields.Boolean(string="active", default=True)

    res_user_id = fields.Many2one(
        "res.users", string="Salesperson", default=lambda self: self.env.user
    )
    partner_id = fields.Many2one(
        "res.partner", string="Customer", change_default=True, index=True
    )
    company_id = fields.Many2one(
        "res.company", store=True, default=lambda self: self.env.company
    )

    # Constraints of the Program

    _sql_constraints = [
        (
            "email_unique",
            "unique (email)",
            "Email must be unique, please choose another.",
        )
    ]
    participants_count = fields.Integer(compute="count_participants")

    # methods of the program

    @api.model_create_multi
    def create(self, vals_list):  # vals_list come in list form
        try:
            for vals in vals_list:
                if vals["height"] == 0:
                    vals["height"] = 5.5
        except Exception as e:
            print("\n\n\nException: \n\n\n", e)
        res_ids = super(StudentInfo, self).create(vals_list)
        return res_ids

    def write(self, vals):  # vals come in the dict form
        if self.height:
            vals.update({"height": 5.5})
        res = super(StudentInfo, self).write(vals)
        return res

    def unlink(self):
        # in self the current profile database data are coming
        print("self profile data", self)
        res = super(StudentInfo, self).unlink()
        print("data delete is", res)

    def student_action_confirm(self):
        print("self data ", self)
        for rec in self:
            print("length of self ", len(self))
            print("rec name", rec)
            rec.state = "confirm"

    def student_action_cancel(self):
        for rec in self:
            rec.state = "cancel"

    def student_action_reset(self):
        for rec in self:
            rec.state = "draft"

    # def teacher_action(self):
    #     self.create({"teacher_ids": [
    #                 (0, 0, {"name": "xyz", "teacher_school_id": "9"}),
    #                 (0, 0, {"name": "abc", "teacher_school_id": "6"})]})

    def student_action_search(self):
        for rec in self:
            # search method
            print(rec.search([], limit=5, order="name desc"))
            print(rec.search([("name", "like", "Dhrumil")]))
            print(rec.search([("birthdate", ">=", "5/4/2000")]))
            students = self.env["student.info"].search([])
            male_student = self.env["student.info"].search(
                [("gender", "=", "male")], order="name desc", limit=5
            )
            female_student = self.env["student.info"].search(
                [("gender", "=", "female")]
            )
            below_9_standard_male_student = self.env["student.info"].search(
                [("gender", "=", "male"), ("standard", "<=", "9")]
            )
            print("all students: ", students)
            print("male students: ", male_student)
            print("female students: ", female_student)
            print("below_9_standard_male_student: ", below_9_standard_male_student)

            # search_count method

            male_student_count = self.env["student.info"].search_count(
                [("gender", "=", "male")]
            )
            print("male_student_count : ", male_student_count)

            # create method

            # student_dict = {
            #     'name':'Aesha patel',
            #     'roll_number':17,
            #     'gender':'female'
            # }
            # self.env['student.info'].create(student_dict)

            # write method
            browse_id = self.env["student.info"].browse(19)
            if browse_id.exists():
                updated_data = {
                    "age": 20,
                    "contact_number": "7799300577",
                    "standard": "5",
                }
                browse_id.update(updated_data)
                print("Successfully update")
            else:
                print("NOoooooooooo")

            """environment test"""
            stud_obj = self.env["student.info"]
            print("\n\n\n\nstudent data\n\n\n\n", stud_obj)
            print(stud_obj.search([]))  # List of ID come
            for stud in stud_obj.search([]):
                print(stud.name)

    @api.onchange("teacher_id")
    def set_teacher_subject(self):
        for rec in self:
            if rec.teacher_id:
                rec.teacher_subject = rec.teacher_id.subject

    """This is compute method of (school_medium) that change medium depends on (standard)"""

    @api.depends("standard")
    def set_student_medium(self):
        for rec in self:
            if rec.standard:
                if int(rec.standard) < 6:
                    rec.school_medium = "primary"
                elif int(rec.standard) >= 6 and int(rec.standard) < 10:
                    rec.school_medium = "secondary"
                else:
                    rec.school_medium = "higher_secondary"

    """age field compute method for calculate age depends on birthdate field"""

    @api.depends("birthdate")
    def get_student_age(self):
        today_date = datetime.date.today()
        for stud in self:
            if stud.birthdate:
                birthdate = fields.Datetime.to_datetime(stud.birthdate).date()
                age_count = str(int((today_date - birthdate).days / 365))
                stud.age = age_count
            else:
                stud.age = "birtdate not provided"

    """This default_get is used for apply default value to multiple fields by function"""

    @api.model  # method is use for make default parameter in field using method
    def default_get(self, fields_list=[]):  # field_list return set of all fields
        print("field list", fields_list)
        rtn = super(StudentInfo, self).default_get(fields_list)
        # rtn return default contain fields only
        rtn["student"] = True
        rtn["standard"] = "5"
        print("default fields", rtn)
        return rtn

    def add_participants(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "name": "Participants",
            "view_mode": "tree,form",
            "res_model": "participants.info",
            # 'domain': [('driver_id', '=', self.id)],
            # 'domain': [('events','=','cvgh')],
            # 'context': {'stu_name': self.id}
            "domain": [],
            "context": {"stu_name": self.id},
        }

    def count_participants(self):
        for participants in self:
            participants.participants_count = self.env[
                "participants.info"
            ].search_count([])
            # self.env['participants.info'].search_count([])

    def _get_portal_return_action(self):
        """Return the action used to display orders when returning from customer portal."""
        self.ensure_one()
        return self.env.ref("school_management.student_data_view")

    def _get_report_base_filename(self):
        self.ensure_one()
        return "%s" % (self.name)

    def cron_demo_method(self):
        self.env["student.info"].search(
            [("birthdate", "=", fields.date.today())]
        ).write({"active": False})

    # browse method :
    # obj = self.env['student.info']
    # data = obj.browse(3)
    # data.exists()

    # fields_get :
    # stud_obj = self.env['student.info'].fields_get()
    # result -> stud_obj = {'field-name':{'parameter':'value'}}


# [{'state': 'draft', 'name': 'Aesha patel', 'birthdate': False, 'standard': '10',
#  'roll_number': 18, 'age': 0, 'gender': 'female', 'contact_number': False, 'image': False,
#   'address': False, 'height': 0, 'aadhar_card': False, 'email': False,
#    'newdate': False, 'blood_group': False, 'teacher_id': 4, 'sport_ids': [[6, False, [4]]],
#     'student_note': False,
#  'teacher_note': False, 'attendence': 0, 'internal_mark': 0, 'final_mark': 0, 'teacher_ids': []}]
