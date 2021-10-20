# -*- coding: utf-8 -*-
{
    "name": "Construction Site",
    "summary": """
       This is Construction site module""",
    "description": """ This is Construction site module
    """,
    "author": "Komal Jimudiya",
    "website": "http://www.aktivesoftware.com",
    "category": "construction",
    "version": "14.0.1.0.0",
    "depends": [
        "sale_management",
        "hr",
        "contacts",
        "stock",
        "purchase",
        "analytic",
        "account",
    ],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/sale_smart_button.xml",
        "views/purchase_smart_button.xml",
        "views/project_smart_button.xml",
        "views/construction_site_views.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
    "sequence": 6,
}
