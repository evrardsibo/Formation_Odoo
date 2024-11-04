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
# from odoo import models, fields
#
# class ResPartner(models.Model):
#     _inherit = 'res.partner'
#
#     contact_type = fields.Selection([
#         ('student', 'Élève'),
#         ('teacher', 'Professeur'),
#         ('tutor', 'Titulaire'),
#         ('admin', 'Secrétariat/Direction'),
#         ('other', 'Autre')
#     ], string='Type de Contact', required=True)
#
#     class_id = fields.Many2one('school.class', string='Classe')
#     option_ids = fields.Many2many('school.option', string='Options')
#     course_ids = fields.Many2many('school.course', string='Cours Suivis')
#
# class SchoolClass(models.Model):
#     _name = 'school.class'
#
#     name = fields.Char(string='Nom de la Classe', required=True)
#     tutor_id = fields.Many2one('res.partner', string='Titulaire', domain=[('contact_type', '=', 'tutor')])
#     degree = fields.Selection([...], string='Degré')
#     student_ids = fields.One2many('res.partner', 'class_id', string='Élèves')
#
# class SchoolCourse(models.Model):
#     _name = 'school.course'
#
#     name = fields.Char(string='Nom du Cours', required=True)
#     teacher_id = fields.Many2one('res.partner', string='Professeur', domain=[('contact_type', '=', 'teacher')])
#     course_type = fields.Selection([...], string='Type de Cours')
#     hours = fields.Float(string='Nombre d\'Heures')
#     degree = fields.Selection([...], string='Degré')
#
# class SchoolProgram(models.Model):
#     _name = 'school.program'
#
#     name = fields.Char(string='Nom du Programme', required=True)
#     course_ids = fields.Many2many('school.course', string='Cours')
#     total_hours = fields.Float(string='Total d\'Heures', compute='_compute_total_hours')
#
#     def _compute_total_hours(self):
#         for program in self:
#             program.total_hours = sum(course.hours for course in program.course_ids)


