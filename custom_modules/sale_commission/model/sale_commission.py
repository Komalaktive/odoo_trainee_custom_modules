# -*- encoding: utf-8 -*-

from odoo import _, fields, models
from odoo.exceptions import UserError


class SaleCommission(models.Model):
    _name = "sale.commission"
    _description = "Sale Commission"
    _rec_name = "user_id"

    order_id = fields.Many2one("sale.order", string="Order")
    user_id = fields.Many2one("res.users", required=True, string="Employee")
    company_id = fields.Many2one(
        "res.company", string="Company", default=lambda self: self.env.company
    )
    currency_id = fields.Many2one("res.currency", related="company_id.currency_id")
    commission_amount = fields.Monetary(string="Commision", required=True)
    commission_type = fields.Selection(
        [("fix", "Fix"), ("percentage", "Percentage")],
        string="Commision Type",
        default="fix",
    )
    state = fields.Selection(
        [("draft", "Draft"), ("paid", "Paid")],
        default="draft",
        string="Status",
        readonly=True,
    )
    move_id = fields.Many2one("account.move", string="Move", readonly=True)
    payment_id = fields.Many2one("account.payment", string="Payment", readonly=True)

    def action_create_employee_payment(self):
        """This method is used for create the employee payment from multiple commission user"""
        user_ids = self.mapped("user_id").ids
        if len(user_ids) > 1:
            raise UserError(_("Please select one employee."))

        states = self.mapped("state")
        if "paid" in states:
            raise UserError(_("This commission entries is already payment."))

        commission_recs = self.env["sale.commission"].browse(
            self._context.get("active_ids")
        )
        amounts = commission_recs.mapped("commission_amount")

        for commission in commission_recs:
            ctx = self._context.copy()
            ctx.update(
                {
                    "active_model": "sale.commission",
                    "active_ids": self.ids,
                    "default_payment_type": "outbound",
                    "default_employee_id": commission.user_id.employee_id.id,
                    "default_partner_id": commission.user_id.partner_id.id,
                    "default_amount": sum(amounts),
                    "default_journal_id": self.env["account.journal"]
                    .search([("type", "=", "bank")], limit=1)
                    .id,
                }
            )
            return {
                "name": _("Payments"),
                "type": "ir.actions.act_window",
                "res_model": "account.payment",
                "view_mode": "form",
                "context": ctx,
            }

    def open_commission_payment(self):
        """This method is used for create the employee payment from commission form view"""
        ctx = self._context.copy()
        ctx.update(
            {
                "active_model": "sale.commission",
                "active_ids": self.id,
                "default_payment_type": "outbound",
                "default_employee_id": self.user_id.employee_id.id,
                "default_partner_id": self.user_id.partner_id.id,
                "default_amount": self.commission_amount,
                "default_journal_id": self.env["account.journal"]
                .search([("type", "=", "bank")], limit=1)
                .id,
            }
        )
        return {
            "name": _("Payments"),
            "type": "ir.actions.act_window",
            "res_model": "account.payment",
            "view_mode": "form",
            "context": {"ctx": ctx},
        }

    def unlink(self):
        """This method use for raise error when delete paid commmission."""
        if "paid" in self.mapped("state"):
            raise UserError(_("You cannot delete paid commission."))
        return super(AccountAccount, self).unlink()
