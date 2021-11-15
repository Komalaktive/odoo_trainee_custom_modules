from odoo import http
from odoo.http import request
import portal

class PaymentPortal(portal.PortalPayment):
    @http.route(["/my/check_existing_order","//my/check_existing_order/<int:page>"],  type='http', auth="user", website=True)



