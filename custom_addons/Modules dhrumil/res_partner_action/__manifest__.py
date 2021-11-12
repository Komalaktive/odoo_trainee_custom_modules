# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Res Partner Action',
    'version': '14.0.1.0.0',
    'category': '',
    'description': """
New Action add into the action menu of res.partner model.
===================================================
""",
    'depends': ['contacts', ],
    'data': [
        "wizard/res_partner_action_menu_views.xml",
        "security/ir.model.access.csv",
    ],
    'demo': [
        
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
}
