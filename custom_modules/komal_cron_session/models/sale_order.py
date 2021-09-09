from odoo import models, fields, api


class Saleorder(models.Model):
    _inherit = "sale.order"


    @api.model
    def demo_cron(self):
        print("\n\n\n\ncron called------")
        Saleorder = self.search([('state', 'not in',('sale','done'))])
        print("\n\n\n\n\n\n", Saleorder)