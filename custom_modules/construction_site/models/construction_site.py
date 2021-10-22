from odoo import api, fields, models


class constructionSite(models.Model):
    _name = "construction.site"
    _description = "Construction Site"
    _rec_name = "display_name"

    name = fields.Char(string="Name", required="True")
    reference = fields.Char(string="Construction Site Code")
    scheduled_date = fields.Datetime(string="Material Requirement")
    state = fields.Selection(
        string="Status",
        default="draft",
        readonly=True,
        copy=False,
        selection=[
            ("draft", "Draft"),
            ("running", "Running"),
            ("stop", "Stopped"),
            ("in_closing", "In Clossing"),
            ("close", "Closed"),
        ],
    )

    responsible_internal_id = fields.Many2one(
        "hr.employee", string="Internal Responsible "
    )
    responsible_on_site_id = fields.Many2one(
        "res.partner", string="Onsite Responsible "
    )
    delivery_address = fields.Many2one("res.partner", string="Delivery Address")
    display_name = fields.Char(
        string="Display Name", compute="_compute_display_name", store="True"
    )
    product_template_id = fields.Many2one("product.template")
    stock_warehouse_id = fields.Many2one("stock.warehouse")
    project_id = fields.Many2one("project.project")
    purchase_order_ids = fields.Many2many("purchase.order", string="purchase")
    # analytical_account_id = fields.Many2one("analytical.account")
    sale_order_id = fields.Many2one("sale.order")
    # asset_id = fields.Many2many(
    #     "account.asset", "asset_id", "ab_id", "purchase_id", string="Asset"
    # )
    general_contractor_purchase_order_id = fields.Many2one("purchase.order")

    @api.depends("reference", "name")
    def _compute_display_name(self):
        if self.reference and self.name:
            for con in self:
                con.display_name = f"[{con.reference}] {con.name}"

    def action_run(self):
        self.state = "running"

    def action_stop(self):
        self.state = "stop"

    def action_in_close(self):
        self.state = "in_closing"

    def action_close(self):
        self.state = "close"

    def action_draft(self):
        self.state = "draft"
