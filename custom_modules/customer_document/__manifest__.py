# -*- coding: utf-8 -*-
{
    "name": "Customer Document",
    "summary": """
        This module is used for create customer document """,
    "description": """
        This is module is used for create customer document 
    """,
    "author": "Komal Jimudiya",
    "website": "https://www.aktivsoftware.com/",
    "category": "Document",
    "version": "14.0.1.0.0",
    "depends": ["contacts", "website","mail"],
    "data": [
        "security/ir.model.access.csv",
        "data/customer_document_menu.xml",
        "views/customer_document_views.xml",
        "views/customer_document_templates.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "sequence": 12,
}
