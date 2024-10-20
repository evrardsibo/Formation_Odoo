from odoo import models, fields, api


class Kitchen(models.Model):
    _name = 'kitchen'
    _description = 'kitchen'

    first_name = fields.Char(string="first_name", required=True)
    last_name = fields.Char(string="last_name", required=True)
    description = fields.Text('Description')
    is_cooked = fields.Boolean(string="Cooked", default=True)
    age = fields.Integer(help="age")
    cook_number = fields.Integer(help="age")
    start_date = fields.Datetime(string="Start Date")
    email = fields.Char(string="Email")
    waiter = fields.Integer(help="waiter")
    total_employees = fields.Integer(string="total_employees", compute="_compute_total_employee", store=True)

    @api.depends('cook_number', 'waiter')
    def _compute_total_employee(self):
        for record in self:
            record.total_employees = (record.cook_number or 0) + (record.waiter or 0)

    @api.onchange('cook_number')
    def _onchange_is_cooked(self):
        for record in self:
            if record.cook_number <= 5:
                record.description = "Moins de 5 personnes"
            elif record.cook_number <= 10:
                record.description = "Moins de 10 personnes"
            elif record.cook_number <= 15:
                record.description = "Moins de 15 personnes"
            else:
                record.description = "Plus de 15 personnes"



