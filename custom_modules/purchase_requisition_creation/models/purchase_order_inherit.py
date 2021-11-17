from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    PR_ref = fields.Char(string='PR Reference', readonly="1")
    purchase_expected_delivery_date = fields.Date(string="Expected Delivery Date")


