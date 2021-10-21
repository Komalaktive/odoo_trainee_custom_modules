from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def construction_site_action(self):
        pass
