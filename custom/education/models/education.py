from odoo import models, fields


class Education(models.Model):
    _name = 'education'
    _description = 'Education'

    contact = fields.Many2one('res.partner',string='Contact')
    type = fields.Selection(selection=[('educateur de rue','Educateur de Rue'),('educateur de quartier','Educateur de Quartier')],string='Type',default='educateur de rue')
    name = fields.Char(string="nick_name", required=True)
    competences = fields.Many2many('competence.tag',string='Competences')