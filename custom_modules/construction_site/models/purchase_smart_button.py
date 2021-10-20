from odoo import models, fields, api


class AddSmartbutton(models.Model):
    _inherit = "purchase.order"

    def construction_list(self):
        print("################open_view_construction_list")

        return {
            "name": "construction",
            "type": "ir.actions.act_window",
            "view_type": "list",
            "view_mode": "list",
            "view_id": self.env.ref("construction_site.construction_site_list").id,
            "res_model": "construction.site",
        }
