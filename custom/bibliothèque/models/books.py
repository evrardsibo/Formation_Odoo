from odoo import models, fields


class Books(models.Model):
    _name = "books"
    description = 'Gestion de bibliothèque'
    _rec_name = 'title'

    title = fields.Char(string="Title")
    author = fields.Many2one('author', string="Author")
    gender = fields.Many2many('genre.tag', string='Gender')
    year_of_manufacture = fields.Date(string="Year of manufacture")
    isbn = fields.Char(string="ISBN")
    copy_number = fields.Integer(string="Copy number")
    image = fields.Image(string='Image')
    sequence = fields.Integer(string="sequence")
    rent_ids = fields.One2many('library.loan','book_id',String='Rent')

    def action_open_wizard_book(self):
        return {
            'name': 'Book Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'book.wizard',
            'view_mode': 'form',
            'target': 'new',
        }
