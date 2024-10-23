from odoo import models , fields


class CompetenceTag(models.Model):
    _name = "genre.tag"
    _description = "Genre Tag"

    name = fields.Char(string="Gender Tag")
    color = fields.Integer(string="Color")