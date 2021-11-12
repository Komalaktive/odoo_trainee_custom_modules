# -*- coding: utf-8 -*-
{
    "name": "School",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    "description": """""",
    "author": "My Company",
    "website": "http://www.yourcompany.com",
    "category": "Uncategorized",
    "version": "14.0.1.0.0",
    "depends": ["base", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/student_views.xml",
        "views/teacher_views.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
