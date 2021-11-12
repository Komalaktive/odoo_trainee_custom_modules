# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Purchase order line',
    'version': '14.0.1.0.0',
    'category': '',
    'description': """
In purchse order line, field add and also ot show in invoice lines.
===================================================
""",
    'depends': ['purchase', 'stock', ],
    'data': [
        "views/purchase_order_line_field_views.xml",
        "views/account_move_line_field_views.xml",
        "views/purchase_order_field_views.xml",
        "views/account_move_field_views.xml",
    ],
    'demo': [
        
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
