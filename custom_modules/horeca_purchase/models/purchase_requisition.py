# -*- coding: utf-8 -*-
import random

from odoo import models, fields, api
import datetime


class PurchaseRequisition(models.Model):
    _name = 'purchase.requisition'
    _inherit = 'purchase.requisition'
    _description = 'Horeca Inherit Purchase Requisition'

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)',
         'Name of the purchase must be unique!')
    ]

    name = fields.Char(readonly=False)
    month = fields.Char()
    week = fields.Char()
    afix = fields.Char()

    @api.onchange("vendor_id", "month", "week", "afix")
    def _onchange_compute_name(self):
        today = datetime.datetime.now()
        m = today.month
        y = today.year
        if self.month and int(self.month) < m and int(self.month) != 0:
            year = str(y + 1)[-2:]
        else:
            year = str(y)[-2:]

        self.name = f'{self.vendor_id.prefix}-{year}/{self.month}/{self.week}/{self.afix}'
