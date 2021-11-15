# -*- coding: utf-8 -*-
{
    "name": "Employees Information",
    "summary": """
        This module is used for create Employees Registration form """,
    "description": """
        This module is used for create Employees Registration form
    """,
    "author": "Komal Jimudiya",
    "website": "https://www.aktivsoftware.com/",
    "category": "Employees",
    "version": "14.0.1.0.0",
    "depends": ["contacts", "hr_recruitment", "mail", "website"],
    "data": [
        "security/ir.model.access.csv",
        "data/create_employees_menu.xml",
        "data/employee_detail_menu.xml",
        "views/create_employees_views.xml",
        "views/hr_job_inherit_views.xml",
        "views/create_employees_template.xml",
        "views/employees_detail_template.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "sequence": 1,
}
