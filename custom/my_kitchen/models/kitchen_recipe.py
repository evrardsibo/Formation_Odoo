from odoo import models, fields


class KitchenRecipe(models.Model):
    _name = 'kitchen.recipe'  #### nom hyper important, sera appelé par le views et le csv
    _description = 'Ceci est un modèle de recette de cuisine'

    name = fields.Char(string='Nom de la Recette')
    description = fields.Text(string='Description')
    cooking_time = fields.Integer(string='Temps de Cuisson')
    instructions = fields.Text('Instructions')
    serving_size = fields.Integer(string='Nombre de Portions')
    image = fields.Image(string='Image')
    line_ids = fields.One2many("recipe.line", "recipe_id", string="Line Id")

    def action_open_wizard_recipe(self):
        return {
            'name': 'Recipe Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'recipe.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_name': self.name,
                        'default_description': self.description,
                        'default_cooking_time': self.cooking_time,
                        'default_serving_size': self.serving_size,
                        },
        }

    # def _get_report_values(self, recids):
    #     recipes = self.env['kitchen.recipe'].browse(recids)
    #
    #     return {
    #         'doc_ids' : recids,
    #         'doc_model':'kitchen.recipe',
    #         'docs':recipes,
    #     }