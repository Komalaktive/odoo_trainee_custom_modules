# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Dhrumil 25042000',
    'version': '14.0.1.0.0',
    'category': '',
    'description': """
Odoo practical test
===================================================
""",
    'depends': ['sale_management', 'website_sale', ],
    'data': [
        "security/requirement_gathering_security.xml",
        "security/ir.model.access.csv",
        "views/product_product_qty_on_order_field_views.xml",
        "views/sale_order_total_capacity_field_views.xml",
        "views/sale_order_line_max_qty_allowed_field_views.xml",
        "views/requirement_gathering_views.xml",
        "views/business_type_views.xml",
        "views/requirement_gathering_template.xml",
        "views/submit_success_template.xml",
        "data/demo_data.xml",
        "data/website_menus.xml",
        "views/menuitems.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
