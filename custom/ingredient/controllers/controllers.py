# -*- coding: utf-8 -*-
# from odoo import http


# class Ingredient(http.Controller):
#     @http.route('/ingredient/ingredient', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ingredient/ingredient/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ingredient.listing', {
#             'root': '/ingredient/ingredient',
#             'objects': http.request.env['ingredient.ingredient'].search([]),
#         })

#     @http.route('/ingredient/ingredient/objects/<model("ingredient.ingredient"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ingredient.object', {
#             'object': obj
#         })

