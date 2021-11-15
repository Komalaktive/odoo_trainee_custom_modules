from datetime import date

from odoo import api, fields, models
from odoo.exceptions import UserError


class CustomerDocument(models.Model):
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _name = "customer.document"
    _description = "This is customer document form"
    _rec_name = "name"

    name = fields.Char(string="Name", required=True, related="customer_name_id.name")
    birth_date = fields.Date(string="Birth Date", tracking=True)
    expiry_date = fields.Date(string="Expiry Date")
    age = fields.Char(string="Age", readonly="1")
    customer_name_id = fields.Many2one("res.partner", string="Customer Name")
    state = fields.Selection(
        string="Status",
        default="draft",
        readonly=True,
        copy=False,
        selection=[
            ("draft", "Draft"),
            ("approved", "Approved"),
            ("expired", "Expired"),
            ("refused", "Refused"),
        ],
    )
    document_count = fields.Integer(
        string="Document count", compute="compute_total_document_count"
    )

    @api.onchange("expiry_date")
    def _compute_date(self):
        if self.expiry_date == date.today():
            self.write({"state": "expired"})

    def action_draft(self):
        self.state = "draft"

    def action_approved(self):
        self.state = "approved"

    def action_expired(self):
        self.state = "expired"

    def action_refused(self):
        self.state = "refused"

    def compute_total_document_count(self):
        for document in self:
            document.document_count = self.env["customer.document"].search_count([])

    def calculate_age(self):
        for record in self:
            if record.birth_date:
                age = date.today().year - record.birth_date.year
                record.age = str(age) + " years"
                if age < 18:
                    raise UserError("The customer age cannot be less than 18 years.")
            else:
                raise UserError("Please select birth date than calculate age.")
