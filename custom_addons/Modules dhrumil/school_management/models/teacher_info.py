from odoo import api, fields, models


class TeacherInfo(models.Model):
    _name = "teacher.info"
    _inherit = ["portal.mixin"]
    _description = "teacher Information"

    def _compute_access_url(self):
        super(TeacherInfo, self)._compute_access_url()
        for tea in self:
            tea.access_url = "/teacher/data/%s" % (tea.id)

    name = fields.Char(string="Name", required=True)
    teacher_school_id = fields.Char(string="Teacher ID", required=True, default="0")
    subject = fields.Char(string="Subject")
    experience = fields.Float(string="Experience")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("others", "Others")], string="Gender"
    )
    email = fields.Char(string="Email")
    student_ids = fields.One2many("student.info", "teacher_id")
    user_id = fields.Many2one("res.users", default=lambda self: self.env.user)

    """ Constraints of the Program """

    _sql_constraints = [
        (
            "id_unique",
            "unique (teacher_school_id)",
            "ID already exists, choose another.",
        )
    ]

    # methods of the program

    def name_get(self):
        teacher_list = []
        for teacher in self:
            teacher_list.append((teacher.id, "{},{}".format(teacher.name, teacher.teacher_school_id)))
        return teacher_list

    @api.model  # used for create new record in dropdown field
    def name_create(self, name):
        print("self data", self)
        res = super(TeacherInfo, self).name_create(name)
        print("res data", res)

    def _get_report_base_filename(self):
        self.ensure_one()
        return "%s" % (self.name)

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100):
        domain = []
        args = args or []
        if name:
            domain = ['|', '|', ('name', operator, name), ('teacher_school_id', operator, name), ('subject', operator, name)]
        return self._search(domain + args, limit=limit)
