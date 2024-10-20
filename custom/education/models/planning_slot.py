from odoo import models, fields


class PlanningSlot(models.Model):
    _inherit = "planning.slot"

    educator_id = fields.Many2one(
        "education",
        string="Educator")
