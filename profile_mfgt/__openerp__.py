# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'Profile MFGT Online Team',
    'version': '9.0.0.1.2',
    'author': 'Hucke Media GmbH & Co. KG/IFE GmbH',
    'category': 'Custom',
    'website': 'https://www.hucke-media.de/',
    'licence': 'AGPL-3',
    'summary': 'Customizations for MFGT',
    'depends': [
        'report',
        'account',
        'sale',
        'purchase',
        'crm',
    ],
    'data': [
        'report/layouts.xml',
        'report/reports.xml',
        'report/report_saleorder.xml',
        'report/report_purchasequotation.xml',
        'report/report_purchaseorder.xml',
        'report/report_invoice.xml',
        'data/report_paperformat.xml',
        'report/product_label.xml',
        'views/sale_order.xml',
    ],
    'installable': True,
    'application': False,
}
