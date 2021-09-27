from odoo import models, fields, api


class SpecialCommand(models.Model):
    _inherit = "sale.order"

    custom_partner_ids = fields.Many2many(
        "res.partner",
        "update_partner_rel",
        "partner_id",
        "update_id",
        string="partners",
    )

    def update_many2many(self):
        print("\n\n update many2many")

        # (0, 0, { values }) -- link to a new record that needs to be created with the given values dictionary
        partner_list = []
        for partner in range(1, 4):
            partner_dict = {"name": partner, "phone": 123456789}
            partner_list.append(partner_dict)
        for val in partner_list:
            self.custom_partner_ids = [(0, 0, val)]

        # replace
        self.custom_partner_ids = [(6, 0, [11, 23])]

        # update
        self.custom_partner_ids = [(1, 23, {"mobile": "8899774422", "name": "xyz"})]

        # add record
        self.custom_partner_ids = [(4, 28)]

        # unclick the record
        self.custom_partner_ids = [(5,)]

        # (calls unlink on ID, that will delete the object completely, and the link to it as well)
        self.custom_partner_ids = [(2, 44)]

        # Remove record from relational field but not parmenent
        self.custom_partner_ids = [(3, 45)]
