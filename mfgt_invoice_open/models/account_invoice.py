# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


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
                rec.action_cancel()