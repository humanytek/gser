from odoo import api, fields, models, _
from odoo.exceptions import UserError

class AccountMoveCompensation(models.Model):
    _inherit = "account.move"
    
    payments = fields.Float(string='Pagos',default="0", readonly=False)
    payment_id = fields.Many2one('account.payment', string="Payment")
    
    

class AccountPayment(models.Model):
    _inherit = "account.bank.statement"
    
    partner_id = fields.Many2one('res.partner', default=False , string='Partner',)
    # invoice_payment_ids = fields.One2many('account.move','partner_id',  string='Facturas')
    invoice_payment_ids = fields.Many2many('account.move', string='Facturas')
    partner_id = fields.Many2one('res.partner', default=False , string='Partner',)
    # payments = fields.Float(string='Pago')
    is_compensation = fields.Boolean(string="Compensación" , default=False, help="Verificar si es una compensación.",)
    journal_id_payment = fields.Many2one('account.journal' , string='Diario de pago : ',)
    amount = fields.Monetary(string='Importee', compute="_compute_importe")
    
    @api.onchange('invoice_payment_ids',)
    def _compute_importe(self):
        if self.is_compensation:
            payments_count = len(self.invoice_payment_ids)
            amount_total = 0
            amount_total_paid = 0
            for i in range(payments_count):
                amount_total += self.invoice_payment_ids[payments_count -1].amount_total
                amount_total_paid += self.invoice_payment_ids[payments_count -1].payments
                payments_count = payments_count - 1
            self.line_ids.amount = amount_total - amount_total_paid
                    
    @api.onchange('is_compensation','line_ids',)
    def _compute_partner(self):
        if self.is_compensation:
            if not self.line_ids.filtered(lambda line: line.partner_id):
                self.write({'is_compensation': False})
                self.is_compensation = False
                error_msg = 'No ha seleccionado un Proveedor en las líneas de transacciones para continuar con la compensación.'
                raise UserError(error_msg)    
            elif self.line_ids.filtered(lambda line: line.partner_id):
                self.partner_id = self.line_ids[0].partner_id.id
                #solo permite agregar una linea en trasacciones
                
    def button_partial_payment(self):
        # res = super(AccountPayment, self).button_post()

        if self.is_compensation:
            list_payment = []
            for statement in self:
                for invoice in statement.invoice_payment_ids:
                    # Obtén el monto de pago de la factura (campo payments en la vista)
                    payment = statement.invoice_payment_ids.filtered(lambda inv: inv.id == invoice.id).payments
                    if payment > 0:
                        payment = self.env['account.payment'].create({
                            'payment_type': 'inbound',
                            'partner_id': invoice.partner_id.id ,
                            'date': statement.date,
                            'amount': payment,
                            'ref': invoice.display_name,
                            'journal_id': statement.journal_id_payment.id,
                            'l10n_mx_edi_payment_method_id': statement.line_ids.l10n_mx_edi_payment_method_id,
                            'currency_id' : self.currency_id.id,
                        })
                        invoice.payment_id = payment.id
                        list_payment.append(invoice.payment_id.id)
            self.process_payments() 
        # return res
    @api.model
    def process_payments(self):
        # Utiliza list_payment directamente aquí
        if self.is_compensation:
            list_payment = []
            for statement in self:
                for invoice in statement.invoice_payment_ids:
                    payment = statement.invoice_payment_ids.filtered(lambda inv: inv.id == invoice.id).payments
                    if payment > 0:
                        list_payment.append(invoice.payment_id.id)
            pending_payments = self.env['account.payment'].browse(list_payment)
            for payment in pending_payments:
                payment.write({'state': 'posted'})
                
    def action_bank_reconcile_bank_statements(self):
        res = super(AccountPayment, self).action_bank_reconcile_bank_statements()
        if self.is_compensation:
            print("SE ESTA CONCILIANDO EL ESTADO DE CUENTA DE COMPENSACION>>>>>>>>>>>>>>>>>>")
            # self.ensure_one()
            # limit = int(self.env["ir.config_parameter"].sudo().get_param("account.reconcile.batch", 1000))
            # bnk_stmt_lines_date = bank_stmt_lines.create_date.strftime('%Y/%m/%d')
            # date_rec = self.date.strftime('%Y/%m/%d')
            bank_stmt_lines = self.env['account.bank.statement.line'].search([
                ('statement_id', 'in', self.ids),
                ('is_reconciled', '=', False),
                ('move_id.display_name', 'ilike', self.invoice_payment_ids[0].name),
            ], limit=100)
            return {
                'type': 'ir.actions.client',
                'tag': 'bank_statement_reconciliation_view',
                'context': {'statement_line_ids': bank_stmt_lines.ids, 'company_ids': self.mapped('company_id').ids},
            }
        return res
        # else:
        #     self.ensure_one()
        #     limit = int(self.env["ir.config_parameter"].sudo().get_param("account.reconcile.batch", 1000))
        #     bank_stmt_lines = self.env['account.bank.statement.line'].search([
        #         ('statement_id', 'in', self.ids),
        #         ('is_reconciled', '=', False),
        #     ], limit=limit)
        #     return {
        #         'type': 'ir.actions.client',
        #         'tag': 'bank_statement_reconciliation_view',
        #         'context': {'statement_line_ids': bank_stmt_lines.ids, 'company_ids': self.mapped('company_id').ids},
        #     }