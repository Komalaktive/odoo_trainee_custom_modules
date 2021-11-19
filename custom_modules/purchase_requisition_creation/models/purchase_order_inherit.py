from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    PR_ref = fields.Char(string='PR Reference', readonly="1")
    purchase_expected_delivery_date = fields.Datetime(string="Expected Delivery Date")
    purchase_pr_no = fields.Char(string="PR Line No")


