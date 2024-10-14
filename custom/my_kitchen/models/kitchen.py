from odoo import models, fields


class Kitchen(models.Model):
    _name = 'kitchen'
    _description = 'Kitchen'

    first_name = fields.Char(string="first_name", required=True)
    last_name = fields.Char(string="last_name", required=True)
    is_cooked = fields.Boolean(string="Cooked",default=True)
    age = fields.Integer(help="age")
    cook_number = fields.Integer(help="Number")
    start_date = fields.Datetime(string="Start Date")
    email = fields.Char(string="Email")