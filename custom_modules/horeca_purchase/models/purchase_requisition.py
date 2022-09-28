# -*- coding: utf-8 -*-
import random

from odoo import models, fields, api


class PurchaseRequisition(models.Model):
    _name = 'purchase.requisition'
    _inherit = 'purchase.requisition'
    _description = 'Horeca Inherit Purchase Requisition'

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)',
         'Name of the purchase must be unique!')
    ]

    month = fields.Char()
    week = fields.Char()
    afix = fields.Char()

    @api.onchange("vendor_id", "month", "week", "afix")
    def _onchange_compute_name(self):
        if self.month and int(self.month) < self.date_order.month and int(self.month) != 0:
            year = str(self.date_order.year + 1)[-2:]
        else:
            year = str(self.date_order.year)[-2:]

        self.name = f'{self.vendor_id.prefix}-{year}/{self.month}/{self.week}/{self.afix}'
