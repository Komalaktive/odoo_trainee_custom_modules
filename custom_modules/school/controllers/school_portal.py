from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo import fields, http
from odoo.exceptions import AccessError, MissingError
from odoo.http import request

class CustomerPortal(CustomerPortal):

    @http.route(['/my/school/portal', '/my/quotes/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_records(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        print("\n\n\n===========IN PYTHON CONTROLLER")
        data = {}
        return request.render("school.portal_my_home_menu_school", data)
