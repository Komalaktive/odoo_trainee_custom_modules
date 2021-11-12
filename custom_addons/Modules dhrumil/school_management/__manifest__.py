# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "School Management",
    "version": "14.0.1.0.0",
    "category": "",
    "summary": "Student details",
    "description": """
This module contains all the common details of student.
    """,
    "depends": ["base", "website", "contacts", "sale_management"],
    "data": [
        "data/school_management_demo_data.xml",
        "security/school_management_security.xml",
        "security/ir.model.access.csv",
        "views/student_info.xml",
        "views/teacher_info.xml",
        "views/res_partner_view.xml",
        "views/sports_info.xml",
        "views/event_participants.xml",
        "views/student_website_list_view.xml",
        "views/teacher_website_list_view.xml",
        "views/sport_website_list_view.xml",
        "views/website_home_menus.xml",
        "views/res_partner_view_with_pagination.xml",
        "views/filter_menu_page_view.xml",
        "views/res_partner_position_attribute_views.xml",
        "data/website_menus.xml",
        "data/cron_demo.xml",
        "report/student_report.xml",
        "report/student_report_card.xml",
        "report/teacher_report.xml",
        "report/teacher_report_card.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}
