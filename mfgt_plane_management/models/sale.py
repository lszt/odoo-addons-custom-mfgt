# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    plane_id = fields.Many2one('mfgt.plane.management', string='Plane', readonly=True, states={'draft': [('readonly', False)]})
    plane_special_information = fields.Text('Special Information')

    @api.onchange('partner_id')
    def select_planes_for_partner(self):
        res = {}
        if self.partner_id:
            res['domain'] = {'plane_id': [('owner_id', '=', self.partner_id.id)]}
        return res

    @api.onchange('plane_id')
    def add_info_to_information(self):
        if self.plane_id:
            self.plane_special_information = self.plane_id.notes
