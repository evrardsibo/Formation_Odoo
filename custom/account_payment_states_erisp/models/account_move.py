from odoo import api,fields, models, _
from odoo.exceptions import UserError, ValidationError
from odoo import models, fields, api, _, Command
from odoo.exceptions import UserError, ValidationError
from odoo.tools.misc import format_date, formatLang



class AccountMove(models.Model):
    _inherit = "account.move"

    state = fields.Selection([
                                ('draft', 'Draft'),
                                ('check', 'Checked'),
                                ('posted', 'Posted'),
                                ('cancel', 'Cancelled')
                             ])
    # state_a = fields.Selection(related='state')
    # state_b = fields.Selection(related='state')
    check_uid = fields.Many2one('res.users', string='Checked By')

    def action_check(self):
        for rec in self:
            rec.check_uid = rec._uid
            rec.state = 'check'

            existance_history = self.history_ids.filtered(lambda h: h.action == 'check')
            existance_history.unlink()

            rec.history_ids.create({
                                        'move_id': self.id,
                                        'action': 'check',
                                    })

    # def toggle_can_edit(self):
    #     for rec in self:
    #         if rec.state == 'check':
    #             if rec.move_type == 'out_invoice' and not self.env.user.has_group('account_erisp.group_account_receivable_approve'):
    #                 rec.can_edit = False
    #             elif rec.move_type == 'in_invoice' and not self.env.user.has_group('account_erisp.group_account_payable_approve'):
    #                 rec.can_edit = False
    #             else: rec.can_edit = True
    #         else:
    #             return super(AccountMove, self).toggle_can_edit()
    

    def previous_state_button(self):
        field_info = self.fields_get(['state'])
        selection_values = field_info['state']['selection']
        keys = [item[0] for item in selection_values]

        for rec in self:
            index = keys.index(rec.state)
            rec.state = keys[index-1]

            existance_history = self.history_ids.filtered(lambda h: h.action == 'back')
            existance_history.unlink()

            rec.history_ids.create({
                                        'move_id': self.id,
                                        'action': 'back',
                                    })

    def action_open_payments(self):
        self.ensure_one()
        domain = ['|',('ref', '=', self.name),('ref','=',self.name)]
        if self.ref:
            domain = ['|',('ref', '=', self.ref),('ref','=',self.name)]
        if self.payment_reference:
            domain = ['|',('ref', '=', self.payment_reference),('ref','=',self.name)]
        return {
                    'name': _("Payments"),
                    'type': 'ir.actions.act_window',
                    'res_model': 'account.payment',
                    'context': {'create': False},
                    'view_mode': 'list,form',
                    'domain': domain 
               }

    def action_open_moves(self):
        self.ensure_one()
        domain = ['|',('line_ids.move_id.ref', '=', self.name),('ref','=',self.name)]
        if self.ref:
            domain = ['|',('ref','=',self.name),('line_ids.move_id.ref', '=', self.ref),('move_type','=','entry')]
        if self.payment_reference:
            domain = ['|',('line_ids.move_id.ref', '=', self.payment_reference),('ref','=',self.name)]

        return {
                    'name': _("Journal Entries"),
                    'type': 'ir.actions.act_window',
                    'res_model': 'account.move',
                    'context': {'create': False},
                    'view_mode': 'list,form',
                    'domain': domain    
               }



        


