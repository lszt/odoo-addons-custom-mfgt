# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re
import uuid

from odoo import api, models

from stdnum import iso11649
from stdnum.iso7064 import mod_97_10

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.multi
    def _get_computed_reference(self):
        def _calculate_reference(inv):
            digit = mod_97_10.calc_check_digits(inv + "RF")
            code = "RF" + digit + inv
            iso11649.validate(code)
            return iso11649.compact(code)

        self.ensure_one()
        if self.reference_type == 'structured':
            seq_suffix = self.journal_id.sequence_id.suffix or ''
            regex_number = '.*?([0-9]+)%s$' % seq_suffix
            exact_match = re.match(regex_number, self.number)
            if exact_match:
                identification_number = int(exact_match.group(1))
            else:
                ran_num = str(uuid.uuid4().int)
                identification_number = int(ran_num[:5] + ran_num[-5:])

            return _calculate_reference("99" + str(identification_number))
        else:
            return super(AccountInvoice, self)._get_computed_reference()
