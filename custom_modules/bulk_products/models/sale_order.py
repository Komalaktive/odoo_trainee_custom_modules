from odoo import models, fields, api


class SaleOreder(models.Model):
    _inherit = "sale.order"

    bulk_product_template_id = fields.Many2one("bulk.products", string="Bulk Products")