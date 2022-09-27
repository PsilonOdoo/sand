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

    @api.onchange("vendor_id", "x_studio_month", "x_studio_week", "x_studio_afix")
    def _onchange_compute_name(self):
        if self.x_studio_month and int(self.x_studio_month) < self.date_order.month and int(self.x_studio_month) != 0:
            year = str(self.date_order.year + 1)[-2:]
        else:
            year = str(self.date_order.year)[-2:]

        self.name = f'{self.vendor.x_studio_numbering_prefix_1}-{year}/{self.x_studio_month}/{self.x_studio_week}/{self.x_studio_afix}'
