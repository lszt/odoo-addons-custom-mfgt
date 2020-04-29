# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import models, api, _
from odoo.exceptions import Warning


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.onchange('reference')
    def _check_duplicate_vendor_reference(self):
        if self.type in ('in_invoice', 'in_refund') and self.reference:
            if self.search([('type', '=', self.type), ('reference', '=', self.reference), ('company_id', '=', self.company_id.id), ('commercial_partner_id', '=', self.commercial_partner_id.id)]):
                raise Warning(_("Duplicated vendor reference detected. You probably encoded twice the same vendor bill/refund."))

    @api.multi
    def invoice_validate(self):
        """Disabled duplicate reference check"""
        return self.write({'state': 'open'})
