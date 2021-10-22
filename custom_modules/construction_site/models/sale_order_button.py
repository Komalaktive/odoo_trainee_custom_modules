from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def construction_site_action(self):
        pass
