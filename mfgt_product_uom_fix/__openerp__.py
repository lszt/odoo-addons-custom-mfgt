# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'MFGT Product uom fix',
    'version': '9.0.1.0',
    'website' : 'http://syscoon.com',
    'category': 'Sales',
    'description': """
Fixed the problem to change an product unit after it has been already used in an account journal item
    """,
    'depends' : [
        'account',
        'product',
    ],
    'data': [
    ],
    'installable': True,
    'auto_install': False,
}