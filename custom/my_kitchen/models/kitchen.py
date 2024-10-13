from odoo.odoo import models, fields


class Kitchen(models.Model):
    _name = 'kitchen.kitchen'
    _description = 'Kitchen'

    first_name = fields.Char(string="<NAME>", required=True)
    last_name = fields.Char(string="<NAME>", required=True)
    is_cooked = fields.Boolean(string="Cooked",default=True)
    age = fields.Integer(help="age")
    cook_number = fields.Integer(help="Number")
    start_date = fields.Datetime(string="Start Date")
    email = fields.Char(string="Email")