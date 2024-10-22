from odoo import models, fields


class KitchenOrder(models.Model):
    _name = 'kitchen.order'
    _description = 'Kitchen Order'

    customer_name = fields.Char(string='Customer Name',required=True)
    order_date = fields.Datetime(string='Order Date',required=True)
    status = fields.Selection(selection=[('preparation','Preparation'),('confirmed','Confirmed'),('delivered','Delivered')],string='Status',default='preparation')
    total_amount = fields.Float(string='Total Amount')