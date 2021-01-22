# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api
from openerp.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def _compute_invoice_zero(self):
        for rec in self:
            if not rec.amount_total and rec.state == 'paid':
                self.invoice_zero = True

    invoice_zero = fields.Boolean('Is Invoice with amout Zero', compute='_compute_invoice_zero')

    @api.multi
    def set_state_open(self):
        for rec in self:
            if rec.invoice_zero:
                moves = self.env['account.move']
                for inv in rec:
                    if inv.move_id:
                        moves += inv.move_id
                    if inv.payment_move_line_ids:
                        raise UserError(_('You cannot cancel an invoice which is partially paid. You need to unreconcile related payment entries first.'))
                self.write({'state': 'cancel', 'move_id': False})
                if moves:
                    # second, invalidate the move(s)
                    moves.button_cancel()
                    # delete the move this invoice was pointing to
                    # Note that the corresponding move_lines and move_reconciles
                    # will be automatically deleted too
                    moves.unlink()