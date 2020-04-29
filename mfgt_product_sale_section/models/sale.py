# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.multi
    @api.onchange('product_id')
    def product_id_change_layout(self):
        if self.product_id.categ_id.sale_layout_id:
            self.sale_layout_cat_id = self.product_id.categ_id.sale_layout_id

    @api.model
    def create(self, vals):
        product_id = self.env['product.product'].browse(vals['product_id'])
        if product_id.categ_id.sale_layout_id:
            vals['sale_layout_cat_id'] = product_id.categ_id.sale_layout_id.id
        res = super(SaleOrderLine, self).create(vals)
        return res