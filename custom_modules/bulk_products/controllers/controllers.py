# -*- coding: utf-8 -*-
# from odoo import http


# class BulkProducts(http.Controller):
#     @http.route('/bulk_products/bulk_products/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bulk_products/bulk_products/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bulk_products.listing', {
#             'root': '/bulk_products/bulk_products',
#             'objects': http.request.env['bulk_products.bulk_products'].search([]),
#         })

#     @http.route('/bulk_products/bulk_products/objects/<model("bulk_products.bulk_products"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bulk_products.object', {
#             'object': obj
#         })
