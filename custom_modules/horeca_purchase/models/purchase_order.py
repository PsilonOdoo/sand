# -*- coding: utf-8 -*-
import random

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _name = 'purchase.order'
    _inherit = 'purchase.order'
    _description = 'Horeca Inherit Purchase'

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)',
         'Name of the purchase must be unique!')
    ]

    @api.onchange('requisition_id')
    def _compute_name_from_purchase_agreement(self):
        if not self.requisition_id:
            return

        count = len(self.requisition_id.purchase_ids.mapped("id"))

        self.name = self.requisition_id.name + '/' + str(count + 1)

    @api.onchange('requisition_id')
    def _compute_agent_from_purchase_agreement(self):
        if not self.requisition_id:
            return

        self.partner_id = self.requisition_id.vendor_id
