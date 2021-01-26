# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = ['account.move', 'portal.mixin', 'mail.thread', 'mail.activity.mixin']