# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'MFGT Plane Management',
    'version': '12.0.1.0',
    'website' : 'http://syscoon.com',
    'category': 'Sales',
    'description': """
Management Tool for Aircraft Planes
    """,
    'depends' : [
        'account','sale',
        'profile_mfgt',
    ],
    'data': [
        'security/ir.model.access.csv',
        'reports/report_saleorder_document.xml',
        'reports/report_invoice_document.xml',
        'views/mfgt_plane_management.xml',
        'views/res_partner.xml',
        'views/sale.xml',
        'views/account.xml',
    ],
    'installable': True,
    'auto_install': False,
}
