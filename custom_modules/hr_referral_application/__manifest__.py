{
    "name": "Hr Referral Application",
    "summary": """
       This is hr referral application form""",
    "description": """ This is hr referral application form """,
    "author": "Komal Jimudiya",
    "website": "https://www.aktivsoftware.com/",
    "category": "Hr",
    "version": "14.0.1.0.0",
    "depends": ["hr_recruitment", "website"],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "data/hr_referral_menu.xml",
        "views/hr_referral_application.xml",
        "views/hr_referral_application_template.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "sequence": 2,
}
