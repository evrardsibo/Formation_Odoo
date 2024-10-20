from odoo import api,fields, models, _
from odoo.exceptions import UserError, ValidationError

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def check_button(self):

        for rec in self:
            rec.state = 'check'

    # def action_post(self):
    #     ''' draft -> posted '''

    #     move_line_record = self.env['account.move.line'].search([('move_id.name','=',self.ref)])
    #     print("AAAAAAAAAAAAAAAAa")

    #     if move_line_record:
    #         print("BBBBBBBBBBBBBBBBB")
    #         if self.partner_type == 'customer':
    #             print("CCCCCCCCCCCCCCCCCCC")

    #             if self.payment_type == 'inbound':
    #                 print("DDDDDDDDDDDDDDDDDDD")

    #                 move_line = move_line_record[0]
    #             else:
    #                 move_line = move_line_record[-1]

    #         if self.partner_type == 'supplier':
    #             if self.payment_type == 'outbound':
    #                 move_line = move_line_record[-1]
    #             else:
    #                 move_line = move_line_record[0]
            
    #         to_process = [{
    #                         "to_reconcile": move_line,
    #                         "payment": self, 
    #                     }]
        
        
    #         payments = self.env['account.payment']

    #         for vals in to_process:
    #             payments |= vals['payment']

    #         payments.move_id._post(soft=False)
          

    #         domain = [
    #             ('parent_state', '=', 'posted'),
    #             ('account_type', 'in', ('asset_receivable', 'liability_payable')),
    #             ('reconciled', '=', False),
    #         ]

    #         for vals in to_process:
    #             print("YYYYYYYY : ",vals['payment'].line_ids)
    #             payment_lines = vals['payment'].line_ids.filtered_domain(domain)
    #             print("WWWWWWWWWW : ",payment_lines)
    #             lines = vals['to_reconcile']
    #             print("BBBBBBBBBBB : ",payment_lines)


    #             for account in payment_lines.account_id:
                    
    #                 (payment_lines + lines)\
    #                     .filtered_domain([('account_id', '=', account.id), ('reconciled', '=', False)])\
    #                     .reconcile()

    #     else:            
    #         self.move_id._post(soft=False)

    def action_post(self):
        ''' draft -> posted '''
        move_line_record = self.env['account.move.line'].search([('move_id.name','=',self.ref)])

        if move_line_record:
            payments = self.env['account.payment']
            to_process = []
            for move_line in move_line_record:
                if move_line.account_id.account_type == 'asset_receivable' and self.payment_type == 'inbound':
                    to_process.append({
                        "to_reconcile": move_line,
                        "payment": self,
                    })
                elif move_line.account_id.account_type == 'liability_payable' and self.payment_type == 'outbound':
                    to_process.append({
                        "to_reconcile": move_line,
                        "payment": self,
                    })

            payments |= self.env['account.payment'].browse([p['payment'].id for p in to_process])
            payments.move_id._post(soft=False)

            # Combine lines with matching accounts for reconciliation
            payment_lines = self.env['account.move.line']
            for vals in to_process:
                domain = [
                    ('parent_state', '=', 'posted'),
                    ('account_type', 'in', ('asset_receivable', 'liability_payable')),
                    ('reconciled', '=', False),
                ]
                payment_lines |= vals['payment'].line_ids.filtered_domain(domain)

            invoice_lines = self.env['account.move.line']
            for vals in to_process:
                invoice_lines |= vals['to_reconcile']

            # Reconcile lines with matching accounts
            for account in invoice_lines.account_id:
                (payment_lines + invoice_lines).filtered_domain([('account_id', '=', account.id), ('reconciled', '=', False)]).reconcile()
        else:
            self.move_id._post(soft=False)

    