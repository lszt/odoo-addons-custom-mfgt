# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import api, fields, models, _
from openerp.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = "product.template"
    
    @api.multi
    def write(self, vals):
        return super(models.Model, self).write(vals)

