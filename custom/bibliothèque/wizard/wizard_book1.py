from odoo import api, fields, models, _


class WizardBook1(models.TransientModel):
    _name = 'book1.wizard'
    _description = 'Create Automatic Book1'

    copy_number = fields.Integer(string="Copy number")
    year_of_manufacture = fields.Date(string="Year of manufacture")

    def create_record_book2(self):
        self.env['books'].create({
            'copy_number': self.copy_number,
            'year_of_manufacture': self.year_of_manufacture,
        })
