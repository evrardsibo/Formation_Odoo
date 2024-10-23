from odoo import models, fields
class Books(models.Model):
    _name = "books"
    description = 'Gestion de bibliothèque'

    title = fields.Char(string="Title")
    author = fields.Char(string="Author")
    gender = fields.Many2many('genre.tag',string='Gender')
    year_of_manufacture = fields.Date(string="Year of manufacture")
    isbn = fields.Integer(string="ISBN")
    copy_number = fields.Integer(string="Copy number")
    image = fields.Image(string='Image')
    sequence = fields.Integer(string="sequence")