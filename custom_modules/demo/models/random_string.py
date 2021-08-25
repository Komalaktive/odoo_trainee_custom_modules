import random
import string
from odoo import api, fields, models
from odoo.tools.translate import _

class ProductTemplate(models.Model):
	_inherit = "product.template"


	random_string =  fields.Char(string=_("Random String"), compute='_compute_random_string',
	                            inverse='_set_random_string')

	@api.depends('product_variant_ids', 'product_variant_ids.random_string')
	def _compute_random_string(self):
		
		unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
		for template in unique_variants:
			template.random_string = template.product_variant_ids.random_string
		

	def _set_random_string(self):
		for template in self:
			if len(template.product_variant_ids) == 1:
				template.product_variant_ids.random_string = template.random_string


	def genrate_random_string(self):
		str = ''.join(random.choices(string.ascii_uppercase + string.digits +string.ascii_lowercase, k = 4))
		print("\n\n\n\nproduct.tamplet\n\n\n\n",str)
		self.update({"random_string": str})      	

class ProductVarients(models.Model):
	_inherit = "product.product"


	random_string = fields.Char(string=_("Random string"))

	def genrate_random_string(self):
		str = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 4))
		print("\n\n\n\nproduct.product\n\n\n\n",str)
		self.update({"random_string": str})      	
