# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Hospital Management",
    "version": "14.0.1.0.0",
    "category": "",
    "summary": "Doctor, Patient, Staff etc. details",
    "description": """
This module contains all the common details of hospital members.
    """,
    "depends": [
        "base",
        "mail",
        "contacts",
        "account",
    ],
    "data": [
        "security/hospital_management_security.xml",
        "security/ir.model.access.csv",
        "views/patient_info.xml",
        "report/patient_report.xml",
        "report/report_card.xml",
        "report/report_invoice_with_payment_inherit.xml",
        "wizard/email_send_wizard_view.xml",
        "data/mail_template.xml",
        "data/demo_cron.xml",
        "data/invoice_due_date_cron.xml",
        "data/invoice_email_template.xml",
        "views/doctor_info.xml",
        "views/account_move_inherit_view.xml",
        "views/res_config_settings_views.xml",
        # 'views/account_move_line_inherit_view.xml',
        "views/patient_data_display.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}
