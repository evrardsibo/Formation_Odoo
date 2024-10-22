from odoo import models, fields, api


class ResPartnerType(models.Model):
    _name = "res.partner.type"
    _description = 'Res Partner Type'

    name = fields.Char(string="Name", required=True, translate=1)
    color = fields.Char(string="Color")
    sequence = fields.Integer(string="Sequence")
    is_confirmed = fields.Boolean(string ="Is Confirmed", default=False)