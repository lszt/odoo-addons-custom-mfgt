# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    plane_id = fields.Many2one('mfgt.plane.management', string='Plane', readonly=True, states={'draft': [('readonly', False)]})
