from odoo import models, fields, api



class KitchenRecipe(models.Model):
    _name = "kitchen.recipe"
    _description = "Kitchen Recipe"

    name = fields.Char(string="Name", required=True)
    description = fields.Text("Description")
    instructions = fields.Text("Instructions")
    cooking_time = fields.Integer(string="Cooking Time")
    serving_size = fields.Integer(string="Serving Size")

    @api.onchange('cooking_time')
    def _onchange_cooking_time(self):
        for rec in self:
            if rec.cooking_time <= 10:
                rec.description = "The kitchen is well equipped for 10 minutes"
            elif rec.cooking_time <= 20:
                rec.description = "The kitchen is well equipped for 20 minutes"
            else:
                rec.description = "The kitchen is equipped for more than 20 minutes"
