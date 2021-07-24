# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _


class MFGTSupplementTypeCertificate(models.Model):
    _name = 'mfgt.plane.stc'
    _description = 'Plane Supplement Management'

    name = fields.Char('Name', required=True)
    description = fields.Char('Description', required=True)


class MFGTMinorChangeApprovals(models.Model):
    _name = 'mfgt.plane.mca'
    _description = 'Plane Management Change Approvals'

    name = fields.Char('Name', required=True)
    description = fields.Char('Description', required=True)

class MFGTPlaneManagement(models.Model):
    _name = 'mfgt.plane.management'
    _description = 'Plane Management'
    _order = 'name asc'

    name = fields.Char('Plante Name', required=True)
    registration = fields.Char('Registration', required=True)
    manufacturer = fields.Char('Producer', required=True)
    type = fields.Char('Type', required=True)
    factory_number = fields.Char('Factory Number', required=True)
    construction_year = fields.Char('Construction Year', required=True)
    tcds_no = fields.Char('TCDS No.', required=True)
    legal_base = fields.Char('Legal Base', required=True)
    registration = fields.Char('Registration', required=True)
    commercial_use = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Commercial Use', required=True)
    noise_level = fields.Char('Noise Level', required=True)
    noise_rate_class = fields.Char('Noise Rate Class', required=True)
    gasoline = fields.Char('Gasoline', required=True)
    max_takeoff_weight = fields.Char('Max. Take Off Weight', required=True)

    engine_manufacturer = fields.Char('Manufacturer', required=True)
    engine_type = fields.Char('Type', required=True)
    engine_number = fields.Char('Number', required=True)
    engine_construction_year = fields.Char('Construction Year', required=True)
    engine_tcds_no = fields.Char('TCDS No.', required=True)

    propeller_manufacturer = fields.Char('Manufacturer', required=True)
    propeller_type = fields.Char('Type', required=True)
    propeller_number = fields.Char('Number', required=True)
    propeller_construction_year = fields.Char('Construction Year', required=True)
    propeller_tcds_no = fields.Char('TCDS No.', required=True)

    supplement_type_certificate_ids = fields.Many2many(comodel_name='mfgt.plane.stc', string='Supplement Type Certificate')

    minor_change_approval_ids = fields.Many2many(comodel_name='mfgt.plane.mca', string='Minor Change Aproval')

    notes = fields.Text('Notes')
    partner_id = fields.Many2one('res.partner', string='Owner')
    owner_id = fields.Many2one('res.partner', string='Owner', required=True)
    sale_ids = fields.One2many('sale.order', 'plane_id', string='Sale Orders')
    next_service = fields.Date('Next Service')
    next_service_type = fields.Char('Service Type')
    arc_expiration = fields.Date('ARC Expiration')
    next_arc_type = fields.Selection([('fr','Full Review'),('ext1','1st Extension'),('ext2','2nd Extension')],'ARC Type')
    last_arc_date = fields.Date('Last ARC')
    last_arc_report = fields.Char('Last ARC Report')
    camo_managed = fields.Boolean('CAMO managed')

    technical_contact_id = fields.Many2one('res.partner', string='Technical Contact')
    technical_contact_phone = fields.Char(related='technical_contact_id.phone', string='Phone')
    technical_contact_phone_company = fields.Char(related='technical_contact_id.phone_company', string='Phone Company')
    technical_contact_mobile = fields.Char(related='technical_contact_id.mobile', string='mobile')
    technical_contact_email = fields.Char(related='technical_contact_id.email', string='Email')

