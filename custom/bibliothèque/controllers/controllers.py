# -*- coding: utf-8 -*-
# from odoo import http


# class Bibliothèque(http.Controller):
#     @http.route('/bibliothèque/bibliothèque', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bibliothèque/bibliothèque/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bibliothèque.listing', {
#             'root': '/bibliothèque/bibliothèque',
#             'objects': http.request.env['bibliothèque.bibliothèque'].search([]),
#         })

#     @http.route('/bibliothèque/bibliothèque/objects/<model("bibliothèque.bibliothèque"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bibliothèque.object', {
#             'object': obj
#         })

