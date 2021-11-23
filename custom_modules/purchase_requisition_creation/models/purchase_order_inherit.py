from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    PR_ref = fields.Char(string="PR Reference", readonly="1")


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    purchase_pr_no = fields.Char(string="PR Line No")
