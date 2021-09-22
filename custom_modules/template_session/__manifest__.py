# -*- coding: utf-8 -*-
{
    'name': "Template Session",
    'summary': """
        Demo module for template session""",
    'author': "Parth Radadia",
    'version': '14.0.1.0.0',    
    'depends': ['website'],
    'license': "AGPL-3",
    'data': [
        'views/demo_template.xml',
        'views/assets.xml',
        'views/inherit_template.xml',
        'data/web_menu_data.xml',

    ],
    'auto_install': False,
    'installable': True,
    'application': True,

}
