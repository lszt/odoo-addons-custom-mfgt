# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    phone_company = fields.Char('Company Phone')
    email2 = fields.Char('Email 2')