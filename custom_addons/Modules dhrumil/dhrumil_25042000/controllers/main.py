from odoo import http, _
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.exceptions import AccessError, MissingError
from collections import OrderedDict
from odoo.http import request


class PortalAccount(CustomerPortal):

    @http.route('/my/requirement', type='http', auth="public", website=True)
    def portal_my_requirement(self, **post):

        # if post:
        #     create_data = {
        #         'email': post.get('email'),
        #         'phone': int(post.get('phone')),
        #         'company': post.get('company'), 
        #         'business_type': post.get('business_type'),
        #         'category': post.get('category'),
        #         'name': f"{post.get('first_name')} {post.get('last_name')}",
        #     }
        #     request.env['requirement.gathering'].sudo().create(create_data)

        business_type = request.env['business.type'].sudo().search([])
        categories = request.env['product.public.category'].sudo().search([])

        vals = {
            'business_type': business_type,
            'categories': categories
        }

        return request.render("dhrumil_25042000.requirement_my_details", vals)

    @http.route('/my/requirement/submit', type='http', auth="public", website=True)
    def portal_submit_success(self, **post):

        if post:
            create_data = {
                'email': post.get('email'),
                'phone': int(post.get('phone')),
                'company': post.get('company'), 
                'business_type': post.get('business_type'),
                'category': post.get('category'),
                'name': f"{post.get('first_name')} {post.get('last_name')}",
            }
            request.env['requirement.gathering'].sudo().create(create_data)

        return request.render("dhrumil_25042000.tmp_customer_form_success", create_data)