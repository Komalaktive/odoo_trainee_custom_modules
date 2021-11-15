from odoo import api, fields, models


class SaleReport(models.AbstractModel):
    _name = "sale.inherit.report"
    _description = "sale report inherit"

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env["inherit.report"].browse(docids)
        return {
            "doc_ids": docs.ids,
            "doc_model": "inherit.report",
            "data": data,
            "docs": docs,
        }
