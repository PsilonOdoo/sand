# -*- coding: utf-8 -*-
import random

from odoo import models, fields, api


class res_partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Horeca res.partner adds partner prefix'

    prefix = fields.Char()