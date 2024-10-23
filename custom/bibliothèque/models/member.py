from odoo import models, fields


class Member(models.Model):
    _name = "member"
    description = 'Gestion de membrer'

    name_id = fields.Many2one("res.partner", string="Name")
    adress = fields.Char(related='name_id.street',string="Adress")
    email = fields.Char(related='name_id.email',string="Email")
    date_start = fields.Date(string="Date Start")
    is_member = fields.Boolean(string="Is Member")
    sequence = fields.Integer(string='Sequence')
    image = fields.Image(related='name_id.image_1920', string="Image")
