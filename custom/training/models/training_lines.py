from odoo import models, fields, api, _
import datetime


class TrainingLine(models.Model):
    _name = "training.line"
    _description = 'Training Line'

    employee_id = fields.Many2one("hr.employee")
    is_present = fields.Boolean(string="Present")
    training_id = fields.Many2one("training")
