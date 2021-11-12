# -*- coding: utf-8 -*-
{
    "name": "Demo",
    "summary": """""",
    "description": """View Inheritance Task""",
    "author": "My Company",
    "website": "http://www.yourcompany.com",
    "category": "Uncategorized",
    "version": "14.0.1.0.0",
    # any module necessary for this one to work correctly
    "depends": [
        "sale",
        "purchase",
    ],
    # always loaded
    "data": [
        "views/product_variant_views.xml",
        "views/sale_order_views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}
