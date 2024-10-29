from odoo import models, fields, _, api


class Education(models.Model):
    _name = 'education'
    _description = 'Education'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    contact = fields.Many2one('res.partner',string='Contact')
    type = fields.Selection(selection=[('educateur de rue','Educateur de Rue'),('educateur de quartier','Educateur de Quartier')],string='Type',default='educateur de rue')
    name = fields.Char(string="nick_name", required=True,default=lambda self: _('New'))
    competences = fields.Many2many('competence.tag',string='Competences')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'education') or _('New')
        record = super(Education, self).create(vals)
        body = "Teacher %s your account is created" % record.name
        record.message_post(body=body)
        return record

    # method to add name automatic in fields

    # method to send msg after creating user

    # @api.model
    # def create(self, vals):
    #     record = super(Education, self).create(vals)
    #     body = "Teacher %s your account is created" % record.name
    #     record.message_post(body=body)
    #     return record