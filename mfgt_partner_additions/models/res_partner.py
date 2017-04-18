# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    phone_company = fields.Char('Company Phone')
    email2 = fields.Char('Email 2')
    x_mfgt_member_number = fields.Integer('MFGT Mitgliedernummer')
    x_mfgt_member_since = fields.Date('MFGT Mitglied seit')
    x_mfgt_member_until = fields.Date('MFGT Mitglied bis')