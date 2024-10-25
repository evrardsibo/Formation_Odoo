from odoo import api, fields, models, _

class WizardRecipe(models.TransientModel):
    _name = 'recipe.wizard'
    _description = 'Create Automatic Recipe'

    name = fields.Char(string='Name')
    description = fields.Text(string='Description')
    cooking_time = fields.Integer(string='Temps de Cuisson')
    serving_size = fields.Integer(string='Nombre de Portions')

    def create_record_recipe(self):
        self.env['kitchen.recipe'].create({
            'name':self.name,
            'description': self.description,
            'cooking_time': self.cooking_time,
            'serving_size': self.serving_size,
        })