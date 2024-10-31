from odoo import models , fields


class CompetenceTag(models.Model):
    _name = "trainer.tag"
    _description = "Trainer Tag"

    name = fields.Char(string="Competence Tag")
    color = fields.Integer(string="Color")