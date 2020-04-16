# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'MFGT Partner Enhancement',
    'version': '12.0.1.0',
    'website' : 'http://syscoon.com',
    'category': 'Sales',
    'description': """
Enhances Partner with several fields.
    """,
    'depends' : [
        'base',
    ],
    'data': [
        'views/res_partner.xml',
    ],
    'installable': True,
    'auto_install': False,
}
