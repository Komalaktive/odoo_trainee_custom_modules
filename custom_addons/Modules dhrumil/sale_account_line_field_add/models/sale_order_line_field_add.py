from odoo import api, fields, models


class SaleOrderLineFieldAdd(models.Model):
    _inherit = "sale.order.line"

    address = fields.Char(string="Address")

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLineFieldAdd, self)._prepare_invoice_line()
        res.update({"address": self.address})
        return res
