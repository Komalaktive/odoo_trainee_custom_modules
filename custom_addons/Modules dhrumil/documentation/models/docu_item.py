from odoo import api, fields, models


@api.model
def _lang_get(self):
    return self.env["res.lang"].get_installed()


class DocumentItem(models.Model):
    _name = "docu.item"
    _description = "Documentation of item's"
    _rec_name = "title"

    title = fields.Char(string="Title", required=True)
    language = fields.Selection(
        _lang_get,
        string="Language"
    )
    active_lang_count = fields.Integer(compute="_compute_active_lang_count")
    description_short = fields.Text(string="Short Description")
    description_long = fields.Html(string="Long Description")
    apps = fields.Many2one("res.partner", string="App")
    version = fields.Many2one("docu.version", string="Version")
    video_url = fields.Char("Video")
    google_document_url = fields.Char("Document")
    tags = fields.Many2many(
        "docu.tags", "item_tags_relation", "item_id", "tag_id", string="Tags"
    )
    active = fields.Boolean(string="Active", default=True)

    """ Compute method of (active_lang_count) field """

    @api.depends("language")
    def _compute_active_lang_count(self):
        lang_count = len(self.env["res.lang"].get_installed())
        for partner in self:
            partner.active_lang_count = lang_count
