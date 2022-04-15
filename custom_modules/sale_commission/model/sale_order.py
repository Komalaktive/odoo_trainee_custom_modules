# -*- encoding: utf-8 -*-

from odoo import _, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    commission_ids = fields.One2many("sale.commission", "order_id")

    def action_sales_commission(self):
        """This method user for create journal entries when user add commission on the sale order"""
        for order in self:
            if order.commission_ids:
                commission_line_ids = order.commission_ids.filtered(
                    lambda line: not line.move_id
                )
                if commission_line_ids:
                    move_lines = self._prepare_commission_move_line(
                        order.commission_ids
                    )
                    move_id = (
                        self.env["account.move"]
                        .sudo()
                        .create(
                            {
                                "journal_id": self.env.ref(
                                    "sale_commission.commission_account_journal"
                                ).id,
                                "line_ids": move_lines,
                                "move_type": "entry",
                            }
                        )
                    )
                    commission_line_ids.write({"move_id": move_id})
                    move_id._post()

    def _prepare_commission_move_line(self, commission_ids):
        """This method used for prepare commission data like credit value ,debit value .. Return list this funcution"""
        commission_account_id = self.env.ref(
            "sale_commission.commission_payable_account"
        ).id
        credit = sum(commission_ids.mapped("commission_amount"))
        move_line_list = [
            (
                0,
                0,
                {
                    "name": "/",
                    "credit": credit,
                    "account_id": commission_account_id,
                },
            )
        ]
        for commission_id in commission_ids:
            if commission_id.commission_type == "fix":
                debit_line_vals = (
                    0,
                    0,
                    {
                        "name": "/",
                        "partner_id": commission_id.user_id.partner_id.id,
                        "debit": commission_id.commission_amount,
                        "account_id": commission_id.user_id.partner_id.property_account_payable_id.id,
                    },
                )
                move_line_list.append(debit_line_vals)

        return move_line_list
