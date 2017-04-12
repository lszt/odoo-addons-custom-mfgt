# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import models, fields, api, _


class MFGTPlaneManagement(models.Model):
    _name='mfgt.plane.management'

    name = fields.Char('Plante Name', required=True)
    registration = fields.Char('Registration', required=True)
    producer = fields.Char('Producer', required=True)
    type_template = fields.Char('Type Template', required=True)
    marketing_designation = fields.Char('Marketing Designation')
    cell = fields.Text('Cell', required=True)
    engine = fields.Text('Engine', required=True)
    propeller = fields.Text('Propeller', required=True)
    gasoline = fields.Char('Gasoline', required=True)
    notes = fields.Text('Notes')
    partner_id = fields.Many2one('res.partner', string='Owner', required=True)
    sale_ids = fields.One2many('sale.order', 'plane_id', string='Sale Orders')
    next_service = fields.Date('Next Service')
    next_service_type = fields.Char('Service Type')
    technical_contact_id = fields.Many2one('res.partner', string='Technical Contact')