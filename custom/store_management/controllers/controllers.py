# -*- coding: utf-8 -*-
# from odoo import http


# class StoreManagement(http.Controller):
#     @http.route('/store_management/store_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/store_management/store_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('store_management.listing', {
#             'root': '/store_management/store_management',
#             'objects': http.request.env['store_management.store_management'].search([]),
#         })

#     @http.route('/store_management/store_management/objects/<model("store_management.store_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('store_management.object', {
#             'object': obj
#         })

