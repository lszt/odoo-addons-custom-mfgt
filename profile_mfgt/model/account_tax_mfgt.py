# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from openerp import api, models


class AccountTaxMFGT(models.AbstractModel):
    _inherit = 'account.tax'
    _rec_name = 'description'
