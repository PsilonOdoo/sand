# -*- coding: utf-8 -*-
# from odoo import http


# class HorecaContacts(http.Controller):
#     @http.route('/horeca_contacts/horeca_contacts', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/horeca_contacts/horeca_contacts/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('horeca_contacts.listing', {
#             'root': '/horeca_contacts/horeca_contacts',
#             'objects': http.request.env['horeca_contacts.horeca_contacts'].search([]),
#         })

#     @http.route('/horeca_contacts/horeca_contacts/objects/<model("horeca_contacts.horeca_contacts"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('horeca_contacts.object', {
#             'object': obj
#         })
