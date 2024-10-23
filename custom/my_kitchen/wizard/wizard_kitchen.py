from odoo import api, fields, models, _

class WizardKitchen(models.TransientModel):
    _name = 'kitchen.wizard'
    _description = 'Create Automatic Kitchen'

    # owner_id = fields.Many2one('res.partner',string='Owner')
    action = fields.Selection([('bonjour', 'Bonjour'), ('bonsoir', 'Bonsoir'), ('hello', 'Hello')], required=True ,default='hello')
    message = fields.Text(string='Message')

