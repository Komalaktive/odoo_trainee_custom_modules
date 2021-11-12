from collections import OrderedDict
from functools import partial

import requests

from odoo import _, fields, http
from odoo.addons.portal.controllers.mail import _message_post_helper
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.addons.portal.controllers.portal import pager as portal_pager
from odoo.exceptions import AccessError, MissingError
from odoo.http import request
from odoo.tools import formatLang


class StudentCount(CustomerPortal):

    MANDATORY_BILLING_FIELDS = [
        "name",
        "phone",
        "email",
        "street",
        "city",
        "country_id",
        "field_creator_name",
        "field_creator_surname",
    ]

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        print("\n\n", values)
        student_count = request.env["student.info"].search_count([])
        teacher_count = request.env["teacher.info"].search_count([])
        sport_count = request.env["sport.info"].search_count([])
        values["stu_count"] = student_count
        values["tea_count"] = teacher_count
        values["spo_count"] = sport_count
        return values

    def _prepare_portal_layout_values(self):
        """Values for /my/* templates rendering.
        Does not include the record counts.
        """
        # get customer sales rep
        sales_user = False
        partner = request.env.user.partner_id
        if partner.user_id and not partner.user_id._is_public():
            sales_user = partner.user_id

        return {
            "sales_user": sales_user,
            "page_name": "home",
        }

    """ student.info, student profile display """

    @http.route(
        ["/student/data/<int:student_id>"], type="http", auth="public", website=True
    )
    def portal_student_page(
        self,
        student_id,
        report_type=None,
        access_token=None,
        message=False,
        download=False,
        **kw
    ):
        try:
            order_sudo = self._document_check_access(
                "student.info", student_id, access_token=access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/student")

        if report_type in ("html", "pdf", "text"):
            return self._show_report(
                model=order_sudo,
                report_type=report_type,
                report_ref="school_management.action_student_id_card",
                download=download,
            )

        values = {
            "student_info": order_sudo,
            "token": access_token,
            "return_url": "/student",
            "bootstrap_formatting": True,
            "report_type": "html",
        }
        values["message"] = message

        return request.render("school_management.student_data_view", values)

    """ student.info list view display """

    @http.route(
        ["/student", "/student/data/<int:page>"],
        type="http",
        auth="public",
        website=True,
    )
    def student_detail(self, sortby=None, filterby=None, **kwargs):
        print("\n\nkwrg\n\n", kwargs)

        error_message = []

        SaleOrder = request.env["student.info"]

        domain = []
        if kwargs and kwargs.get("state") != "all":
            domain += [("state", "=", kwargs.get("state"))]
        if kwargs and kwargs.get("teacher_id"):
            domain += [("teacher_id", "=", int(kwargs.get("teacher_id")))]

        searchbar_sortings = {
            "name": {"label": _("Reference"), "student": "name"},
            "roll_no": {"label": _("roll_no"), "student": "roll_number desc"},
        }
        # default sortby order
        if not sortby:
            sortby = "name"
        sort_order = searchbar_sortings[sortby]["student"]

        searchbar_filters = {
            "all": {"label": _("All"), "teacher": []},
            "stage": {"label": _("Stage"), "teacher": [("state", "in", ["draft"])]},
        }

        if not filterby:
            filterby = "all"
        domain += searchbar_filters[filterby]["teacher"]
        print("domainnnnnnnnnnn", domain)

        values = {
            "page_name": "students",
            "stu_data": SaleOrder.sudo().search(domain, order=sort_order),
            "searchbar_sortings": searchbar_sortings,
            "page_name": "student",
            "sortby": sortby,
            "default_url": "/student",
            "searchbar_filters": OrderedDict(sorted(searchbar_filters.items())),
            "filterby": filterby,
        }

        return request.render("school_management.detail_student_data", values)

    """ teacher.info list view display """

    @http.route(
        ["/teacher", "/teacher/data/<int:page>"],
        type="http",
        auth="public",
        website=True,
    )
    def teacher_detail(
        self, page=1, sortby=None, date_begin=None, date_end=None, **kwargs
    ):

        SaleOrder = request.env["teacher.info"]

        searchbar_sortings = {
            "name": {"label": _("Reference"), "teacher": "name"},
            "teacher_id": {
                "label": _("teacher_id"),
                "teacher": "teacher_school_id desc",
            },
        }
        # default sortby order
        if not sortby:
            sortby = "name"
        sort_order = searchbar_sortings[sortby]["teacher"]

        values = {
            "page_name": "teacher",
            "tea_data": SaleOrder.sudo().search([], order=sort_order),
            "searchbar_sortings": searchbar_sortings,
            "sortby": sortby,
        }
        return request.render("school_management.detail_teacher_data", values)

    """ teacher.info, techer profile display """

    @http.route(
        ["/teacher/data/<int:teacher_id>"], type="http", auth="public", website=True
    )
    def portal_teacher_page(
        self,
        teacher_id,
        report_type=None,
        access_token=None,
        message=False,
        download=False,
        **kw
    ):
        try:
            order_sudo = self._document_check_access(
                "teacher.info", teacher_id, access_token=access_token
            )
        except (AccessError, MissingError):
            return request.redirect("/teacher")

        if report_type in ("html", "pdf", "text"):
            return self._show_report(
                model=order_sudo,
                report_type=report_type,
                report_ref="school_management.action_teacher_id_card",
                download=download,
            )

        values = {
            "teacher_info": order_sudo,
            "token": access_token,
            "return_url": "/teacher",
            "bootstrap_formatting": True,
            "report_type": "html",
        }
        values["message"] = message

        return request.render("school_management.teacher_data_view", values)

    """ filteration view by (state) and (teacher) display """

    @http.route("/filter", type="http", auth="public", website=True)
    def filter_task(self, **kwargs):
        error_message = []
        print("kwargsssssss", kwargs)
        student_env_data = request.env["student.info"]
        stu_vals = dict(student_env_data._fields["state"].selection)
        teachers = request.env["teacher.info"].sudo().search([])
        values = {
            "state": stu_vals,
            "teachers": teachers,
            "page_name": "filter",
        }

        if kwargs:
            domain = []
            if kwargs.get("state") != "all":
                domain += [("state", "=", kwargs.get("state"))]
            if kwargs.get("teacher_id"):
                domain += [("teacher_id", "=", int(kwargs.get("teacher_id")))]
            values.update({"st_data": student_env_data.sudo().search(domain)})

            if values.get("st_data"):
                error_message.append(_('Data found'))
                values.update({"positive_error": error_message})
            else:
                error_message.append(_('Data not found'))
                values.update({"negative_error": error_message})
            # if values.get("st_data"):
            #     return request.render("school_management.detail_student_data", values)
            # else:
            #     error_message.append(_('Data not found'))
            # stu_vals = dict(request.env["student.info"]._fields["state"].selection)
            # teachers = request.env["teacher.info"].sudo().search([])

            # val = {
            #     "state": stu_vals,
            #     "teachers": teachers,
            #     'error': error_message
            # }

            # return requests.post('http://localhost:9999/filter', {'foram': 'foram'})

        return request.render("school_management.detail_filter_data", values)

    """ sport.info list view display """

    @http.route(
        ["/sport", "/sport/data/<int:page>"], type="http", auth="public", website=True
    )
    def sport_detail(
        self, page=1, sortby=None, date_begin=None, date_end=None, **kwargs
    ):

        SaleOrder = request.env["sport.info"]

        searchbar_sortings = {
            "sport_name": {"label": _("sport_name"), "sport": "sport_name"},
            "entry_fee": {"label": _("entry_fee"), "sport": "entry_fee desc"},
        }

        if not sortby:
            sortby = "sport_name"
        sort_order = searchbar_sortings[sortby]["sport"]

        values = {
            "page_name": "sport",
            "sp_data": SaleOrder.sudo().search([], order=sort_order),
            "searchbar_sortings": searchbar_sortings,
            "sortby": sortby,
        }
        return request.render("school_management.detail_sport_data", values)


""" res.partner kanban view with pagination """


class MyCustomWeb(http.Controller):
    @http.route(
        ["/contact", "/contact/page/<int:page>"], type="http", auth="user", website=True
    )
    def contact_kanban(self, page=0, search="", **post):
        domain = []
        if search:
            domain.append(("name", "ilike", search))
        post["search"] = search
        contact_obj = request.env["res.partner"].sudo().search(domain)
        total = contact_obj.sudo().search_count([])
        pager = request.website.pager(
            url="/contact",
            total=total,
            page=page,
            step=12,
        )
        offset = pager["offset"]
        contact_obj = contact_obj[offset : offset + 12]
        return request.render(
            "school_management.contact_form",
            {
                "search": search,
                "contact_details": contact_obj,
                "pager": pager,
            },
        )
