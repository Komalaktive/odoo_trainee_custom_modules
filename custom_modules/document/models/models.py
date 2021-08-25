# -*- coding: utf-8 -*-

from odoo import api, fields, models


class DocuItem(models.Model):
    _name = "docu.item"
    _description = "Document"

    @api.model
    def _selection_languages(self):
        return self.env["res.lang"].get_installed()

    name = fields.Char(string="Name")
    task_name = fields.Char(string="Task Name")
    description_short = fields.Text(string="Short Description")
    description_long = fields.Html(string="Long Description")
    video_url = fields.Char("Video URL", default="www.odoo.com")
    google_url = fields.Char("Google URL")
    doc_type = fields.Selection(
        [("Maths", "Maths"), ("Physics", "Physics"), ("Chemistry", "Chemisty")],
        string="Types of Book",
    )
    lang = fields.Selection(_selection_languages, string="Template Preview Language")
    active = fields.Boolean(string="active", default="True")
    tag = fields.Many2many("docu.type", string="Tag")
    rec_model = fields.Many2one("docu.version", string="Version")
