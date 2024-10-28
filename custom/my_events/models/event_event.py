import datetime
from email.policy import default

from odoo import fields, models, api



class EventEvent(models.Model):
    _name = "event.management"
    _description = 'Event Management'

    name = fields.Char(string='Event Name', required=True)
    description = fields.Text(string='Description')
    date_start = fields.Datetime(default=datetime.date.today(), string='Start Date', required=True)
    date_end = fields.Datetime(default=datetime.date.today()+datetime.timedelta(+7),string='End Date',required=True)
    image = fields.Image(related='responsible_id.image_1920',string='Image')
    responsible_id = fields.Many2one('res.users', string='Responsible')
    employee_ids = fields.Many2many('hr.employee', string='Employees')
    sequence = fields.Integer(string="sequence")
    duration = fields.Float(string='Duration')
