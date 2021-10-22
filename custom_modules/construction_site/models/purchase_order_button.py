from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    construction_site_count = fields.Integer(
        compute="_compute_construction_count", string="Consruction Count"
    )

    def _compute_construction_count(self):
        for site in self:
            site.construction_site_count = self.env["construction.site"].search_count(
                [("general_contractor_purchase_order_id", "=", self.id)]
            )

    def action_view_construction_site(self):
        construction_site = False
        construction_site = self.env["construction.site"].search_count(
            [("general_contractor_purchase_order_id", "=", self.id)]
        )
        print("---------------------", construction_site)
        if construction_site == 1:
            construction_site = (
                self.env["construction.site"]
                .search([("general_contractor_purchase_order_id", "=", self.id)])
                .id
            )
            view_mode = "form"
        else:
            view_mode = "tree"

        return {
            "type": "ir.actions.act_window",
            "view_mode": view_mode,
            "name": "Construction Site",
            "res_model": "construction.site",
            "domain": ([("general_contractor_purchase_order_id", "=", self.id)]),
            "targer": "current",
            "res_id": construction_site,
        }
