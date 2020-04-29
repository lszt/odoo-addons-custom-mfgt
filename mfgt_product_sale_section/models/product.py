# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = 'product.category'

    sale_layout_id = fields.Many2one('sale_layout.category', string='Sale Layout Category')