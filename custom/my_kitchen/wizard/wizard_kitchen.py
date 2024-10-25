from odoo import api, fields, models, _

class WizardKitchen(models.TransientModel):
    _name = 'kitchen.wizard'
    _description = 'Create Automatic Kitchen'

    name = fields.Char(string='Name')
    owner_id = fields.Many2one('res.partner', string='Owner')
    message = fields.Text(string='Message')

    def create_record(self):
        self.env['kitchen'].create({
            'first_name':self.name,
            'owner_id': self.owner_id.id,
        })
