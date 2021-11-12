import random
import string

from odoo import api, fields, models


class ProductTemplate(models.Model):
    # _name = "product.string.generate"
    _inherit = "product.template"

    string_generate = fields.Char(
        string="Random_string",
        compute="_compute_string_generate",
        inverse="_set_string_generate",
    )

    @api.depends("product_variant_ids.string_generate")
    def _compute_string_generate(self):
        self.string_generate = False
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.string_generate = template.product_variant_ids.string_generate

    def _set_string_generate(self):
        if len(self.product_variant_ids) == 1:
            self.product_variant_ids.string_generate = self.string_generate

    def random_string_generate(self):
        all_chars = list(string.ascii_letters)
        random.shuffle(all_chars)

        self.string_generate = "".join(all_chars[:3]).upper() + "-M"


class ProductData(models.Model):
    _inherit = "product.product"

    string_generate = fields.Char(string="Random_string")

    def random_string_generate(self):
        all_chars = list(string.ascii_letters)
        random.shuffle(all_chars)

        self.string_generate = "".join(all_chars[:3]).upper() + "-M"
