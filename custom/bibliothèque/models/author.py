from odoo import models, fields
class Author(models.Model):
    _name = "author"
    _description = 'Author Books'

    name = fields.Char(string='Author')
    sequence = fields.Integer()
