from odoo import models, fields, api,_
import datetime

class Training(models.Model):
    _name ="training"
    _description = 'Training'

    name = fields.Char(string="Name")
    tags = fields.Many2many('trainer.tag',string='Tags')
    supervisor_id = fields.Many2one('res.users', string="supervisor")
    image = fields.Image(related='supervisor_id.image_1920',string='Image')
    line_ids = fields.One2many("training.line", "training_id")
    duration = fields.Integer(string="Duration")
    date_start = fields.Date(default=datetime.date.today(), string='Date', required=True) #computer
    date_end = fields.Date(compute="_add_dynamic_date_end", string='End Date', required=True)


    @api.depends("date_start","duration")
    def _add_dynamic_date_end(self):
        for record in self:
            if record.date_start:
                record.date_end = record.date_start + datetime.timedelta(days=record.duration)


