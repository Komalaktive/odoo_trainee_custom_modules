# -*- coding: utf-8 -*-

from odoo import models, fields, api


class docu_item(models.Model):
    _name = 'docu.item'
    _description = 'Task Mnagement'

    name = fields.Char(string="Student Name")
    description = fields.Text(string="Description")

