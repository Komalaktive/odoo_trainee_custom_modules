# -*- coding: utf-8 -*-
{
    "name": "Template Session",
    "summary": """
        Demo module for template session""",
    "author": "Komal jimudiya",
    "version": "14.0.1.0.0",
    "depends": ["website_sale"],
    "license": "AGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "data/web_menu_data.xml",
        "views/partner_list_template.xml",
        "views/assets.xml",
        "views/inherit_template.xml",
        "views/partner_description_page.xml",
        "views/res_partner_table_views.xml"
    ],
    "auto_install": False,
    "installable": True,
    "application": True,
}
