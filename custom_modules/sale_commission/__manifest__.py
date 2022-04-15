# -*- encoding: utf-8 -*-

{
    "name": "Sale Commission",
    "version": "14.0.1.3.1",
    "category": "sale management,account",
    "summary": """Sale Commission""",
    "description": """Sale Commission""",
    "author": "Aktiv Software",
    "website": "http://www.aktivsoftware.com",
    "depends": ["sale_management", "account_accountant", "hr"],
    "data": [
        "security/ir.model.access.csv",
        # "views/assets.xml",
        "report/wells_sales_html_report.xml",
        "wizard/wells_sales_views.xml",
        "data/account_account_data.xml",
        "views/sale_order_view.xml",
        "views/sale_commission_view.xml",
        "views/account_employee_payment.xml",
    ],
    "installable": True,
    "auto_install": False,
}
