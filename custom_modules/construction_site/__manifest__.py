# -*- coding: utf-8 -*-
{
    "name": "Construction Site",
    "summary": """
       This is Construction site module""",
    "description": """ This module are used to create construction site
    """,
    "author": "Komal Jimudiya",
    "website": "http://www.aktivsoftware.com",
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
        "project",
    ],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/construction_site_views.xml",
        "views/purchase_order_button_views.xml",
        "views/project_task_button_views.xml",
        "views/sale_order_button_views.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
    "sequence": 6,
}
