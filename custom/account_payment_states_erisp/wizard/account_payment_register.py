from odoo import fields, models,api, _
from datetime import datetime
from odoo.exceptions import UserError, ValidationError
import math

import logging

class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    
    def _create_payments(self):
        print("________________Create Payments_____________")
        account_payment = self.env['account.payment'].search([('ref','=',self.communication)])
        if account_payment:
            for record in account_payment:
                if record.state != 'posted':
                    raise ValidationError("Kindly post the previous generated payment first.")


        self.ensure_one()
        batches = self._get_batches()
        edit_mode = self.can_edit_wizard and (len(batches[0]['lines']) == 1 or self.group_payment)
        to_process = []

        if edit_mode:
            payment_vals = self._create_payment_vals_from_wizard(batches[0])
            to_process.append({
                'create_vals': payment_vals,
                'to_reconcile': batches[0]['lines'],
                'batch': batches[0],
            })
        else:
            # Don't group payments: Create one batch per move.
            if not self.group_payment:
                new_batches = []
                for batch_result in batches:
                    for line in batch_result['lines']:
                        new_batches.append({
                            **batch_result,
                            'lines': line,
                        })
                batches = new_batches

            for batch_result in batches:
                to_process.append({
                    'create_vals': self._create_payment_vals_from_batch(batch_result),
                    'to_reconcile': batch_result['lines'],
                    'batch': batch_result,
                })

        # print("________to_process__________")
        # print(to_process)

        payments = self._init_payments(to_process, edit_mode=edit_mode)

        # self._post_payments(to_process, edit_mode=edit_mode)
        
        # self._reconcile_payments(to_process, edit_mode=edit_mode)