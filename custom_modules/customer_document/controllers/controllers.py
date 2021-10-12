# -*- coding: utf-8 -*-
# from odoo import http


# class CustomerDocument(http.Controller):
#     @http.route('/customer_document/customer_document/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/customer_document/customer_document/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('customer_document.listing', {
#             'root': '/customer_document/customer_document',
#             'objects': http.request.env['customer_document.customer_document'].search([]),
#         })

#     @http.route('/customer_document/customer_document/objects/<model("customer_document.customer_document"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('customer_document.object', {
#             'object': obj
#         })
