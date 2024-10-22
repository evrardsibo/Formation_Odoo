from odoo import models, fields, api, _
from odoo.exceptions import UserError


class RecipeLine(models.Model):
    _name = "recipe.line"
    _description = 'Recipe Line'

    ingredient_id = fields.Many2one("ingredient", string="Ingredient")
    quantity = fields.Float(string='Quantity')
    recipe_id = fields.Many2one('kitchen.recipe', string="Recipe Id")
    can_by_pass = fields.Boolean(string='Can By Pass', default=False)

    @api.onchange('quantity')
    def _onchange_max_quantity(self):
        for record in self:
            if record.quantity > record.ingredient_id.quantity_max:
                raise UserError(_("Another user is already created using this email"))
