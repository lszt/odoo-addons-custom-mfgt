# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name' : 'MFGT Sale Section in Product-Category',
    'version': '12.0.1.0',
    'website' : 'http://ife.de',
    'category': 'Hidden/Dependency',
    'depends' : [
            'sale',
            'stock',
            ],
    'description': """
Adds Sale Section in Product-Category which applies automatically in the sale order line.
    """,
    'data': [
        'views/product.xml'
    ],
    'installable': True,
    'auto_install': False,
}
