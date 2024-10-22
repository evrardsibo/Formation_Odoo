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
            if record.quantity > record.ingredient_id.quantity_max and not record.can_by_pass:
                raise UserError(_("More than quantity"))

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            if not val['can_by_pass']:
                ingredient = self.env['ingredient'].browse(val['ingredient_id'])
                if val['quantity'] > ingredient.quantity_max:
                    return UserError(_('Quantity is too more'))

        return super().create(vals_list)

    def write(self, vals):
        for val in vals:
            if 'quantity' in val:
                raise UserError(_('No change possible for the quantity field'))
        return super().write(vals)
