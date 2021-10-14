# -*- coding: utf-8 -*-

{
    'name': 'HR Employee Sequence',
     "summary": """
       This is practice of wizard and ir sequence module""",
    "description": """  This is practice of wizard and ir sequence module""",
    "author": "Komal Jimudiya",
    "website": "https://www.aktivsoftware.com/",
    'version': '14.0.1.0.0',
   
    'category': 'Business',
    'depends': ['hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_view.xml',
        'wizard/practice_wizard_view.xml',
        'views/inherit_sequence_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': 5,
}
