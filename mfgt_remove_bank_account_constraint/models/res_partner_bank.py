# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    _sql_constraints = [
        ('unique_number', 'CHECK (1=1)', 'Account Number must be unique'),
    ]