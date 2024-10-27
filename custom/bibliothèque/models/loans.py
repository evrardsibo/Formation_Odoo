from odoo import models, fields, api
from odoo import exceptions
from datetime import datetime


class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Library Loan'
    _rec_name = "member_id"

    member_id = fields.Many2one('member', string='Member', required=True)
    book_id = fields.Many2one('books', string='Book', required=True)
    loan_date = fields.Date(string='Loan Date', default=fields.Date.context_today, required=True)
    image = fields.Image(related='member_id.image', string="Image")
    return_date = fields.Date(string='Return Date')
    state = fields.Selection([
        ('ongoing', 'Ongoing'),
        ('returned', 'Returned'),
        ('late', 'Late')
    ], string='State', default='ongoing')

    _sql_constraints = [
        (
            'unique_bibliothèque_model',
            'UNIQUE(member_id, book_id, state)',
            'You cannot borrow the same book if it has not been returned.'
        )
    ]

    # @api.constrains('loan_date')
    # def _check_loan_time(self):
    #     for record in self:
    #         loan_time = datetime.strptime(str(record.loan_date), '%Y-%m-%d').time()
    #         if loan_time < datetime.strptime('09:00', '%H:%M').time() or loan_time > datetime.strptime('17:30', '%H:%M').time():
    #             raise exceptions.ValidationError("You can only register a loan between 09:00 and 17:30.")

    @api.constrains('state')
    def _check_unique_loan(self):
        for record in self:
            if record.state in ['ongoing', 'late']:
                """
                self.search_count : Méthode qui compte le nombre d'enregistrements correspondant aux critères fournis.
                """
                if self.search_count([
                    ('member_id', '=', record.member_id.id),
                    ('book_id', '=', record.book_id.id),
                    ('state', '=', 'ongoing'),
                    ('state', 'in', ['ongoing', 'late']),
                ]) > 1:
                    raise exceptions.ValidationError("You cannot borrow the same book if it has not been returned.")
