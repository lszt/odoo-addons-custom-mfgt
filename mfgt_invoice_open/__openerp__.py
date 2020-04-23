# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'MFGT Set Invoice back to Open',
    'version': '12.0.1.0',
    'website' : 'http://syscoon.com',
    'category': 'Accounting',
    'description': """
Mangemant Tool for Aircraft Planes
    """,
    'depends' : [
        'account',
    ],
    'data': [
        'views/account_invoice.xml',
    ],
    'installable': True,
    'auto_install': False,
}
