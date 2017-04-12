# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from openerp import api, models


class DateTimeConverter(models.AbstractModel):
    _inherit = 'ir.qweb.field.datetime'

    @api.model
    def value_to_html(self, value, field, options=None):
        if options and options.get('date_only'):
            return self.env['ir.qweb.field.date'].value_to_html(
                value, field, options=options)
        return super(DateTimeConverter, self).value_to_html(
            value, field, options=options)
