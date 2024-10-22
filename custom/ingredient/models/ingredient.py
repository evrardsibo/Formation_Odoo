from odoo import models, fields


class Ingredient(models.Model):
    _name = 'ingredient'
    _description = 'Ingredient'

    name = fields.Char('name', required=True)
    weight = fields.Float('weight', required=True)
    description = fields.Text('description', required=True)
    quantity_max = fields.Float(string="Quantity Max")


