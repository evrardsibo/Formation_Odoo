from odoo import models, fields


class KitchenRecipe(models.Model):
    _name = 'kitchen.recipe' #### nom hyper important, sera appelé par le views et le csv
    _description = 'Ceci est un modèle de recette de cuisine'

    name = fields.Char(string='Nom de la Recette')
    description = fields.Text('Description')
    cooking_time= fields.Integer(string = 'Temps de Cuisson')
    instructions = fields.Text('Instructions')
    serving_size = fields.Integer(string='Nombre de Portions')
    image = fields.Image(string='Image')
    line_ids = fields.One2many("recipe.line","recipe_id",string="Line Id")