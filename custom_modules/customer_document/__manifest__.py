# -*- coding: utf-8 -*-
{
    'name': "Customer Document",

    'summary': """
        This is customer document form""",

    'description': """
        This is customer document form
    """,
    'author': "Komal Jimudiya",
    'website': "https://www.aktivsoftware.com/",
    'category': 'Document',
    'version': '14.0.1.0.0',
    'depends': ["sale_management"],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_document_views.xml',
        'views/customer_document_templates.xml',
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "sequence": 5,

}
