# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Documentation",
    "version": "14.0.1.0.0",
    "summary": "Documentation data",
    "sequence": 10,
    "description": """  The module contain the documentaion data  """,
    "category": "",
    "website": "",
    "images": [],
    "depends": ["base", "contacts"],
    "data": [
        "security/ir.model.access.csv",
        "data/documentation_demo_data.xml",
        "views/docu_item_view.xml",
        "views/docu_version_view.xml",
        "views/docu_tags_view.xml",
    ],
    "demo": [],
    "qweb": [],
    "installable": True,
    "application": True,
    "auto_install": False,
}
