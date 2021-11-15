import json
from odoo import http
from odoo.http import request, route
from odoo import fields, models, api


class Product(http.Controller):
    @http.route("/products", type="http", website=True, auth="public")
    def demo(self):
        products = request.env["product.template"].sudo().search([])
        return request.render(
            "product_website.product_demo_page", {"products": products}
        )


class ProductDescription(http.Controller):
    @http.route(
        "/product/info/<model('product.template'):product>",
        type="http",
        website=True,
        auth="public",
    )
    def form(self, product, **kw):
        print("=======product====", product)
        return request.render(
            "product_website.product_description_page", {"product": product}
        )
