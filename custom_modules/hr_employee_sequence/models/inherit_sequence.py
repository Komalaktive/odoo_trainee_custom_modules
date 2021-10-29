from odoo import fields, models, api


class Test(models.Model):
    _inherit = "hr.employee"

    sequence = fields.Char()

    @api.model
    def create(self, vals):
        vals["sequence"] = (
            self.env["ir.sequence"].next_by_code("ir.sequence.code") or "New"
        )
        return super(Test, self).create(vals)

    def name_wizard(self):
        pass

    def test_wizard(self):
        context = self._context
        emp = self.env[context['active_model']].browse(context['active_id'])
        emp.mobile_phone = self.name