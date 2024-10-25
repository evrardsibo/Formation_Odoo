from odoo import models, fields

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'
    _rec_name ="member_id"

    member_id = fields.Many2one('member', string='Member', required=True)
    book_id = fields.Many2one('books', string='Book', required=True)
    loan_date = fields.Date(string='Loan Date', default=fields.Date.context_today, required=True)
    image = fields.Image(related='member_id.image',string="Image")
    return_date = fields.Date(string='Return Date')
    state = fields.Selection([
        ('ongoing', 'Ongoing'),
        ('returned', 'Returned'),
        ('late', 'Late')
    ], string='State', default='ongoing')
