# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
{
    'name': 'Profile MFGT - Motorfluggruppe Thurgau',
<<<<<<< HEAD
    'version': '12.0.0.1.9',
=======
    'version': '12.0.0.1.14',
>>>>>>> 61e11ba3504666e9c6cce5fe5adb75217c59d834
    'author': 'Motorfluggruppe Thurgau MFGT',
    'category': 'Custom',
    'website': 'https://www.mfgt.ch/',
    'licence': 'AGPL-3',
    'summary': 'Customizations for MFGT',
    'depends': [
        'account',
        'account_accountant',
        'sale',
        'sale_management',
        'purchase',
        'crm',
        'stock',
        'product',
        'product_expiry',
	'l10n_ch',
	'l10n_ch_reports',
	'mfgt_partner_additions',
	'mfgt_invoice_open',
    ],
    'data': [
       'report/layouts.xml',
       'report/reports.xml',
       'report/report_saleorder.xml',
       'report/report_purchasequotation.xml',
       'report/report_purchaseorder.xml',
       'report/report_invoice.xml',
       'data/report_paperformat.xml',
       'data/account_tags.xml',
       #'data/account_financial_report.xml',
       'report/product_label.xml',
       'views/sale_order.xml',
       'views/stock.xml',
       'report/report_deliveryslip.xml',
    ],
    'installable': True,
    'application': False,
}
