# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, api, models, modules


class Users(models.Model):
    _name = 'res.users'
    _inherit = ['res.users']

    prefix = fields.Char()
