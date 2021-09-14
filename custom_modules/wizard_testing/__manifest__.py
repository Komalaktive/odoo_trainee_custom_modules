# -*- coding: utf-8 -*-
{
    "name": "Wizard Testing",
    "summary": """
        Wizard Practice""",
    "description": """""",
    "author": "Komal Jimudiya",
    "website": "http://www.yourcompany.com",
    "category": "wizard",
    "version": "14.0.1.0.0",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/create_wizard.xml",
        "views/wizard_test.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "sequence": 3,
}
