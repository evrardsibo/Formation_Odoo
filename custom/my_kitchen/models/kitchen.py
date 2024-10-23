from odoo import models, fields, api
from odoo.exceptions import ValidationError

from datetime import date


class Kitchen(models.Model):
    _name = 'kitchen'
    _description = 'kitchen'

    @api.model
    def get_default_date(self):
        return date.today()

    first_name = fields.Char(string="first_name", required=True)
    last_name = fields.Char(string="last_name", required=True)
    description = fields.Text('Description')
    is_cooked = fields.Boolean(string="Cooked", default=True)
    age = fields.Integer(help="age")
    cook_number = fields.Integer(help="age")
    start_date = fields.Date(string="Start Date", default=get_default_date)
    email = fields.Char(string="Email")
    waiter = fields.Integer(help="waiter")
    phone = fields.Integer(string="Phone")
    total_employees = fields.Integer(string="total_employees", compute="_compute_total_employee", store=True)
    owner_id = fields.Many2one('res.partner', string='Owner')
    message = fields.Text(string='Message', compute='_check_owner_id')
    _sql_constraints = [
        (
            'unique_my_kitchen_model',
            'UNIQUE(first_name)',
            'First_name name must be unique'
        )
    ]

    def add_cook_number(self):
        for record in self:
            record.cook_number += 1
            # self.update_description()
            # self.update_waiter()

    def update_waiter(self):
        for record in self:
            record.waiter += 5

    def update_description(self):
        for record in self:
            if record.cook_number <= 5:
                record.description = "Moins de 5 personnes"
            elif record.cook_number <= 10:
                record.description = "Moins de 10 personnes"
            elif record.cook_number <= 15:
                record.description = "Moins de 15 personnes"
            else:
                record.description = "Plus de 15 personnes"

    @api.depends('cook_number', 'waiter')
    def _compute_total_employee(self):
        for record in self:
            record.total_employees = (record.cook_number or 0) + (record.waiter or 0)

    @api.depends('owner_id')
    def _check_owner_id(self):
        for record in self:
            if record.owner_id:
                record.message = f"{record.owner_id.name}"
            else:
                record.message = "Who are you ?"

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

    @api.constrains('cook_number')
    def _check_cook_number(self):
        for record in self:
            if record.cook_number < 0:
                raise ValidationError("The cook_number cannot be negatif")

    def action_open_wizard(self):
        return {
            'name': 'Kitchen Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'kitchen.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'owner_id': self.owner_id.name,
                        'default_message': self.message},

        }
