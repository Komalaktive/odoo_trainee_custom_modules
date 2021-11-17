from odoo import models, fields, api


class PurchaseRequisitionWizard(models.TransientModel):
    _name = "purchase.requisition.wizard"
    _description = "Purchase Requisition wizard"

    reject_reason = fields.Char(string="Reason for Reject", tracking=True)

    def confirm_requisition(self):
        print("\n\n self.env.context", self._context)
        active_mod = self._context.get('active_model')
        active_id = self.env[active_mod].browse(self._context.get('active_id'))
        print("========active id", active_id)
        print("=========self.reject_reason",self.reject_reason)

        display_msg = "<ul>This is the reason of rejection: %s</ul>" % (self.reject_reason)
        active_id.message_post(body=display_msg)

    # sale_order.message_post(body=display_msg)
