from odoo import http
from odoo.http import request, route


class CustomerDocument(http.Controller):
    @route("/customer_document", type="http", website=True, auth="public")
    def customer_document(self):
        customer_name_id = request.env["customer.document"].search([])
        return request.render(
            "customer_document.customer_document_detail_form",
            {"customer_ids": customer_name_id},
        )

    @route("/customer_document_form", type="http", website=True, auth="public")
    def customer_document_form(self):
        customer_name_id = request.env["customer.document"].search([])
        return request.render(
            "customer_document.customer_document_create_page",
            {"customer_name_id": customer_name_id},
        )

    @route("/insert_customer_new_record", type="http", website=True, auth="public")
    def insert_customer_document_record(self, **kw):
        if kw:
            customer_name_id = request.env["res.partner"].search(
                [("id", "ilike", kw["customer_name_id"])]
            )
            vals = {
                "name": kw["name"],
                "customer_name_id": customer_name_id.id,
                "age": kw["age"] + " years",
            }
            request.env["customer.document"].sudo().create(vals)
        return request.render("customer_document.thank_you_template_customer_document")
