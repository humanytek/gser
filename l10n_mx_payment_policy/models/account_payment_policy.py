from odoo import api,fields, models


class AccountPaymentPolicy(models.Model):
    _inherit = "account.move"

        
    @api.depends('move_type', 'invoice_date_due', 'invoice_date', 'invoice_payment_term_id', 'invoice_payment_term_id.line_ids')
    def _compute_l10n_mx_edi_payment_policy(self):
        res = super(AccountPaymentPolicy, self)._compute_l10n_mx_edi_payment_policy()
        for move in self:
            if move.is_invoice(include_receipts=True) and move.invoice_date_due and move.invoice_date:
                if move.move_type == 'out_invoice':
                    # In CFDI 3.3 - rule 2.7.1.43 which establish that
                    # invoice payment term should be PPD as soon as the due date
                    # is after the last day of  the month (the month of the invoice date).
                    if move.invoice_date_due.month > move.invoice_date.month or \
                    move.invoice_date_due.year > move.invoice_date.year or \
                    len(move.invoice_payment_term_id.line_ids) > 1 or \
                    move.invoice_payment_term_id.line_ids.days > 21 :  # to be able to force PPD
                        move.l10n_mx_edi_payment_policy = 'PPD'
                    else:
                        move.l10n_mx_edi_payment_policy = 'PUE'
                else:
                    move.l10n_mx_edi_payment_policy = 'PUE'
            else:
                move.l10n_mx_edi_payment_policy = False
        return res
