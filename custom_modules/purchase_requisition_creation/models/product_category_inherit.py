from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    product_group_id = fields.Many2one("res.users", "Product group", required="1")


# Inherit this method to add access rights in csv
class ProductProduct(models.Model):
    _inherit = "product.product"


# Inherit this method to add access rights in csv
class ProductTemplate(models.Model):
    _inherit = "product.template"
