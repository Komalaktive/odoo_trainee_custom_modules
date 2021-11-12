# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Sale Account line field add",
    "version": "14.0.1.0.0",
    "category": "",
    "summary": "Inside sale lines add field Address",
    "description": """
This module conatin modification of sale.order model.
    """,
    "depends": ["base", "contacts", "sale_management"],
    "data": [
        "views/sale_order_line_field_add_view.xml",
        "views/account_move_line_field_add_view.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}
