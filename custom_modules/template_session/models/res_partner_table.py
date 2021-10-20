from odoo import fields, models, api


class PartnerTeam(models.Model):
    _name = "team.member.table"
    _description = "team member"

    name = fields.Char(related="member_id.name", string="Name")
    email = fields.Char(related="member_id.email", string="Email")
    phone = fields.Char(related="member_id.phone", string="Phone")
    address = fields.Char(related="member_id.contact_address", string="Address")
    partner_id = fields.Many2one("res.partner", string="Contact")

    member_id = fields.Many2one(
        "res.partner", domain="[('team_leader', '=', False)]", string="Member"
    )


class PartnerTask(models.Model):
    _inherit = "res.partner"

    team_ids = fields.One2many("team.member.table", "partner_id", string="Team member")

    team_leader = fields.Boolean(string="TL")
