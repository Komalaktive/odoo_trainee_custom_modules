# -*- coding: utf-8 -*-
# © 2018-Today Aktiv Software (http://www.aktivsoftware.com).
# Part of AktivSoftware See LICENSE file for full copyright
# and licensing details.
{
    "name": "Purchase Requisition Creation & Allocation",
    "category": "Purchase",
    "summary": "Purchase Requisition Creation & Allocation",
    "author": "Aktiv Software",
    "website": "https://www.aktivsoftware.com/",
    "version": "13.0.1.0.0",
    "license": "OPL-1",
    "price": 25.00,
    "currency": "USD",
    "description": "",
    "depends": ["purchase", "stock"],
    "data": [
        "security/purchase_requisition_security.xml",
        "security/ir.model.access.csv",
        "data/purchase_requisition_data.xml",
        "wizard/purchase_requisition_wizard_view.xml",
        "views/purchase_requisition_view.xml",
        "views/product_category_inherit_view.xml",
        "views/purchase_order_inherit_view.xml",
    ],
    "images": ["static/description/banner.jpg",],
    "installable": True,
    "application": False,
}
