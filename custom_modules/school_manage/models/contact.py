# -*- coding: utf-8 -*-

from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = "res.partner"

    active = fields.Boolean(string="active", default=True)
    reviews = fields.Char(string="Reviews")

    def name_get(self):
        result = []
        for account in self:
            result.append(
                (
                    account.id,
                    "{} ({}) {}".format(
                        account.name,
                        account.city,
                        account.property_supplier_payment_term_id.name,
                    ),
                )
            )
        return result

    @api.model
    def _name_search(self, name, args=None, operator="ilike", limit=1):
        args = args or []
        domain = []
        if name:
            domain = ["|", ("name", operator, name), ("city", operator, name)]
        return self._search(args + domain, limit=limit)
