from odoo import api, fields, models, _

class WizardBook(models.TransientModel):
    _name = 'book.wizard'
    _description = 'Create Automatic Book'

    title = fields.Char(string="Title")
    isbn = fields.Integer(string="ISBN")

    def action_open_wizard_book1(self):
        return {
            'name': 'Book Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'book1.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_title': self.title,
                        'default_isbn': self.isbn},

        }
