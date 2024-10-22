from odoo import models, fields



class Partner(models.Model):
    _inherit = 'res.partner'

    is_cook = fields.Boolean('Is Cook')
    type_ids = fields.Many2many("res.partner.type", string="Type")