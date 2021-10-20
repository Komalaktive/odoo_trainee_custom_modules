from odoo import models, fields, api


class AddSmartbutton(models.Model):
    _inherit = "sale.order"

    def construction_site_action(self):
        pass
