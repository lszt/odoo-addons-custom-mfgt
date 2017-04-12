# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    plane_ids = fields.One2many('mfgt.plane.management', 'partner_id', string='Planes')