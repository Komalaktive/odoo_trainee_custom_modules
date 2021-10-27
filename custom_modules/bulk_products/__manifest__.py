# -*- coding: utf-8 -*-
{
    'name': "Bulk Products",

    'summary': """ This is bulk Product module """,

    'description': """  This is bulk Product module """,

    'author': "Komal Jimudiya",
    'website': "http://www.aktivsoftware.com",

    'category': 'products',
    'version': '14.0.1.0.0',

    'depends': ['sale_management', 'purchase', 'contacts','stock'],

    'data': [
        'security/ir.model.access.csv',
        'views/bulk_products_views.xml',
        'views/sale_order_views.xml',
        'views/bulk_products_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
    "sequence": 16,
}
