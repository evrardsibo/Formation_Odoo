from dataclasses import fields

from odoo import models , fields


class CompetenceTag(models.Model):
    _name = "competence.tag"
    _description = "Competence Tag"

    name = fields.Char(string="Competence Tag")
    color = fields.Integer(string="Color")