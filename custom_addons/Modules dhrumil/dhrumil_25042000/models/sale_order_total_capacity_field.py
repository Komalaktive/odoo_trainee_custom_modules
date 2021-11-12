from odoo import fields, models
from odoo.tools.translate import _

class TotalCapacity(models.Model):
    _inherit = "sale.order"

    total_capacity = fields.Char(string=_("Total Capacity"))
    
    def calulate_total_capacity(self):
        res = self.order_line
        total_sum = 0.0
        for r in res:
            total_sum += r.max_qty_allowed
        self.total_capacity = total_sum        
        
    