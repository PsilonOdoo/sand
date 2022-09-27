# -*- coding: utf-8 -*-
# from odoo import http


# class HorecaPurchase(http.Controller):
#     @http.route('/horeca_purchase/horeca_purchase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/horeca_purchase/horeca_purchase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('horeca_purchase.listing', {
#             'root': '/horeca_purchase/horeca_purchase',
#             'objects': http.request.env['horeca_purchase.horeca_purchase'].search([]),
#         })

#     @http.route('/horeca_purchase/horeca_purchase/objects/<model("horeca_purchase.horeca_purchase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('horeca_purchase.object', {
#             'object': obj
#         })
