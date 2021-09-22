# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request, route
from odoo import fields, models, api

class Controller(http.Controller):
    @http.route("/partner/list", type="http", website=True, auth="public")
    def demo_page(self):
        partners = request.env['res.partner'].sudo().search([])
        return request.render("template_session.demo_page", {'partners': partners})

