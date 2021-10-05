from odoo import http
from odoo.http import request, route

class ReferalApplication(http.Controller):
    @http.route("/referral_program", type="http", website=True, auth="user")
    def referral_program(self):
        referral_id = request.env["hr.employee"].sudo().search([])
        degree_id = request.env["hr.recruitment.degree"].sudo().search([])
        dept_id = request.env["hr.recruitment.degree"].sudo().search([])
        vals = {
            'referral_id':referral_id,
            'degree_id':degree_id,
            'dept_id':dept_id,
        }
        return request.render("hr_referral_application.referral_program_template",vals)
    @http.route("/submit_referral_program", type="http", website=True, auth="public")
    def submit_referral_program(self, **post):
        print("===========post========",post)
        if post:
            vals = {
                'name':post.get('name'),
                'email':post.get('email'),
            }
            print("=============vals==============",vals)
            # request.env["hr.referral.application"].sudo().create(vals)

            vals = request.env["hr_referral_application"].sudo().create(vals)
            # request.env["hr.referral.application"].sudo().create(vals)

        return request.render("hr_referral_application.thank_you_template",vals)




