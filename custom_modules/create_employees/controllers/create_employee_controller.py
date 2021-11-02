# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request, route


class ReferralProgram(http.Controller):
    @http.route("/create_employees", type="http", website=True, auth="public")
    def create_employees(self):
        state_id = request.env["res.country.state"].sudo().search([])
        country_id = request.env["res.country"].sudo().search([])
        job_position_id = request.env["hr.job"].sudo().search([])
        vals = {
            "state_id": state_id,
            "country_id": country_id,
            "job_position_id": job_position_id,
        }
        return request.render("create_employees.create_employees_template", vals)

    @http.route("/submit_create_employees", type="http", website=True, auth="public")
    def submit_create_employees(self, **post):
        if post:
            state_id = request.env["res.country.state"].search(
                [("name", "=like", post["state_id"])]
            )
            country_id = request.env["res.country"].search(
                [("name", "=like", post["country_id"])]
            )
            job_position_id = request.env["hr.job"].search(
                [("name", "=like", post["job_position_id"])]
            )
            vals = {
                "name": post["name"],
                "email": post["email"],
                "birth_date": post["birth_date"],
                "street": post["street"],
                "city": post["city"],
                "phone": post["phone"],
                "experience_info": post["experience_info"],
                "expected_salary": post["expected_salary"],
                "state_id": state_id.id,
                "job_position_id": job_position_id.id,
                "country_id": country_id.id,
            }
            request.env["create.employees"].sudo().create(vals)
        return request.render("create_employees.thank_you_template")

    @http.route("/employee_detail", type="http", website=True, auth="user")
    def employee_detail(self):
        document_ids = request.env["create.employees"].search([])
        return request.render(
            "create_employees.create_employees_detail_template",
            {"document_ids": document_ids},
        )
