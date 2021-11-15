# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request, route
from odoo import fields, models, api


class Controller(http.Controller):
    @http.route("/partner/list", type="http", website=True, auth="public", csrf=False)
    def demo_page(self, **kw):
        partners = request.env["res.partner"].sudo().search([])
        if kw:
            print("kw==================", kw)
            vals = {
                "name": kw.get("name"),
                "email": kw.get("email"),
                "phone": kw.get("phone"),
            }
            print("=============vals==============", vals)
            request.env["res.partner"].sudo().create(vals)
        return request.render("template_session.demo_page", {"partners": partners})

    @http.route(
        "/partner/details/<model('res.partner'):partner>",
        type="http",
        website=True,
        auth="public",
        csrf=False,
    )
    def form_list(self, partner, **kw):
        print("=======partner====", partner)
        return request.render(
            "template_session.partner_description_page", {"partner": partner}
        )

    @http.route(
        "/contact/create_new_contact",
        type="http",
        website=True,
        auth="public",
        csrf=False,
    )
    def create_new_contact(self, **kw):
        states = request.env["res.country.state"].sudo().search([])
        countries = request.env["res.country"].sudo().search([])
        return request.render("template_session.create_new_contact",{
                "countries": countries,
                "states": states,
            },
        )
