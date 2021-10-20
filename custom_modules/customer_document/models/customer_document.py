from datetime import date

from odoo import api, fields, models
from odoo.exceptions import UserError


class CustomerDocument(models.Model):
    _name = "customer.document"
    _description = "This is customer document form"
    _rec_name = "name"

    name = fields.Char(string="Name")
    birth_date = fields.Date(string="Birth Date")
    expiry_date = fields.Date(string="Expiry Date")
    age = fields.Integer(string="Age", readonly="1")
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
    document_count = fields.Integer(string="Document count", compute="compute_total_document_count")

    @api.onchange("expiry_date")
    def _compute_date(self):
        print("===================================expireddddddddddddd")
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
        print("============================document=======================")
        for document in self:
            document.document_count = self.env["customer.document"].search_count([])