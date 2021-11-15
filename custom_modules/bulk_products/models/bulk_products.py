from odoo import models, fields, api


class BulkProducts(models.Model):
    _name = 'bulk.products'
    _description = 'This is bulk products module'

    name = fields.Char(string="Name")
    master_product_id =fields.Many2one("product.template", string="Master Product")
    user_id = fields.Many2one("res.partner", string="User")
    email = fields.Char(string="Email")
    bulk_product_template_ids = fields.One2many(
        "bulk.product.template", "bulk_products_id", string="Bulk Products", index=True, tracking=True)



