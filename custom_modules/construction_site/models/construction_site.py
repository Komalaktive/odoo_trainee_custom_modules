from odoo import models, fields


class constructionSite(models.Model):
    _name = "construction.site"
    _description = "Construction Site"

    name = fields.Char(string="Name")
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
            ("stopped", "Stopped"),
            ("inclosing", "In Clossing"),
            ("closed", "Closed"),
        ],
    )

    responsible_internal_id = fields.Many2one(
        "hr.employee", string="Internal Responsible "
    )
    responsible_on_site_id = fields.Many2one(
        "res.partner", string="Onsite Responsible "
    )
    delivery_address = fields.Many2one("res.partner", string="Delivery Address")
    product_template_id = fields.Many2one("product.template")
    stock_warehouse_id = fields.Many2one("stock.warehouse")
    project_id = fields.Many2one("project.project")
    purchase_order_ids = fields.Many2many("purchase.order", string="purchase")
    analytical_account_id = fields.Many2one("analytical.account")
    sale_order_id = fields.Many2one("sale.order")
    asset_id = fields.Many2many(
        "account.asset", "asset_id", "ab_id", "purchase_id", string="Asset"
    )
    general_contractor_purchase_order_id = fields.Many2one("purchase.order")

    # def name_get(self):
    #     print("==================xcbjbcm",self)
    # result = []
    # for combined in self:
    #     display_name = f"[{combined.reference}] {combined.name}"
    #     result.append((combined.id, display_name))
    # return result

    # def name_get(self):
    #     print("+++++++++++++++++++++++++++askjdhbasjdfb",self)
    #     result = []
    #     for rec in self:
    #         demo = '[' + rec.reference + ']' + ' ' + rec.name
    #         result.append((rec.id, demo))
    #     return result

    def name_get(self):
        result = []
        for con in self:
            name = f"[{con.reference}] {con.name}"
            result.append((con.id, name))
        return result

    def action_draft(self):
        self.state = "draft"

    def action_running(self):
        self.state = "running"

    def action_stopped(self):
        self.state = "stopped"

    def action_inclosing(self):
        self.state = "inclosing"

    def action_closed(self):
        self.state = "closed"

