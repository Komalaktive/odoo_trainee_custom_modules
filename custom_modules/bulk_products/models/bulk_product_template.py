from odoo import models, fields, api


class BulkTemplate(models.Model):
    _name = "bulk.product.template"
    _description = "Bulk Product Template"

    bulk_product_field_id = fields.Many2one("product.product", domain="[('type', '=', 'product')]", string="Bulk product")
    bulk_products_id = fields.Many2one("bulk.products", string="Products")