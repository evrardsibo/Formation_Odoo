from odoo import models, fields, api


class Kitchen(models.Model):
    _name = 'kitchen'
    _description = 'Kitchen'

    first_name = fields.Char(string="first_name", required=True)
    last_name = fields.Char(string="last_name", required=True)
    is_cooked = fields.Boolean(string="Cooked", default=True)
    description = fields.Text(string="Description")
    age = fields.Integer(help="age")
    cook_number = fields.Integer(help="Number")
    start_date = fields.Datetime(string="Start Date")
    email = fields.Char(string="Email")
    waiter = fields.Integer(string="Waiter")
    total_employe = fields.Integer(string="Total Employe", compute="_compute_total_employe", store=True)

    @api.depends('cook_number', 'waiter')
    def _compute_total_employe(self):
        for rec in self:
            rec.total_employe = rec.cook_number + rec.waiter

    @api.onchange('cook_number')
    def _onchange_cook_number(self):
        for rec in self:
            if rec.cook_number <= 5:
                rec.description = "The kitchen is well equipped for 5 people"
            elif rec.cook_number <= 10:
                rec.description = "The kitchen is well equipped for 10 people"
            elif rec.cook_number <= 15:
                rec.description = "The kitchen is well equipped for 15 people"
            else:
                rec.description = "The kitchen is equipped for more than 15 people"
