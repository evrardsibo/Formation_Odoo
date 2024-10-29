from datetime import date

from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    active = fields.Boolean(default="True", string="Archive")

    def _archive_after_validate_data(self):
        for record in self.search([]):
            if record.validity_date > date.today():
                return record.active == False





