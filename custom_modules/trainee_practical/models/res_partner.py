from odoo import api, fields, models


class SearchModify(models.Model):
    _inherit = "res.partner"

    def name_get(self):
        result = []
        for partner in self:
            result.append((partner.id, "{} ({})".format(partner.name, partner.city)))

        return result

    @api.model
    def _name_search(self, name, args=None, operator="ilike", limit=100):
        args = args or []
        domain = []
        if name:
            domain = ["|", ("name", operator, name), ("city", operator, name)]
        return self._search(args + domain, limit=limit)
