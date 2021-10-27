# -*- coding: utf-8 -*-
{
    'name': "Student Information",

    'summary': """
        This module is used to student registration Form""",

    'description': """
       This module is used to student registration Form
    """,

    'author': "Komal Jimudiya",
    'website': "http://www.aktivsofware.com",

    'category': 'student',
    'version': '14.0.1.0.0',

    'depends': ['base'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/bulk_products_views.xml',
        'views/bulk_products_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
    "sequence": 14,
}
