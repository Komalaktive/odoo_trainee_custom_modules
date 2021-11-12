# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Product template random string",
    "version": "14.0.1.0.0",
    "category": "",
    "summary": "In product.template random string button create and also in product.product",
    "description": """
This module conatin modification of product.template model.
    """,
    "depends": ["base", "contacts", "sale"],
    "data": [
        "views/random_string_product_view.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}
