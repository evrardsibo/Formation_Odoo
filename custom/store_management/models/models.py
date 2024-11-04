# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class store_management(models.Model):
#     _name = 'store_management.store_management'
#     _description = 'store_management.store_management'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
# pk.eyJ1IjoiZXZha2VuIiwiYSI6ImNtMmh1cjNkejBnOGwyaXNkdzhnaWhhNmcifQ.VfJ9CG25KC2Q7PFeSQrOXw

# from odoo import models, fields
#
# class ResPartner(models.Model):
#     _inherit = 'res.partner'
#
#     contact_type = fields.Selection([
#         ('student', 'Élève'),
#         ('teacher', 'Professeur'),
#         ('principal', 'Titulaire'),
#         ('admin', 'Secrétariat/Direction'),
#         ('other', 'Autre')
#     ], string='Type de Contact')
#
#     class_id = fields.Many2one('school.class', string='Classe', domain="[('contact_type', '=', 'student')]")
#     option = fields.Char(string='Option', domain="[('contact_type', '=', 'student')]")
#     courses = fields.Many2many('school.course', string='Cours suivis', domain="[('contact_type', '=', 'student')]")
#
#     teaching_courses = fields.One2many('school.course', 'teacher_id', string='Cours donnés', domain="[('contact_type', 'in', ['teacher', 'principal'])]")
#
# class SchoolCourse(models.Model):
#     _name = 'school.course'
#     _description = 'Cours'
#
#     name = fields.Char(string='Nom du cours', required=True)
#     type_id = fields.Many2one('school.course.type', string='Type de cours')
#     hours = fields.Integer(string='Nombre d\'heures')
#     degree_id = fields.Many2one('school.degree', string='Degré')
#     teacher_id = fields.Many2one('res.partner', string='Professeur', domain="[('contact_type', '=', 'teacher')]")
#     class_ids = fields.Many2many('school.class', string='Classes')
#
# class SchoolClass(models.Model):
#     _name = 'school.class'
#     _description = 'Classe'
#
#     name = fields.Char(string='Nom de la classe', required=True)
#     principal_id = fields.Many2one('res.partner', string='Titulaire', domain="[('contact_type', '=', 'principal')]")
#     degree_id = fields.Many2one('school.degree', string='Degré')
#     student_ids = fields.One2many('res.partner', 'class_id', string='Élèves')
#     program_ids = fields.Many2many('school.program', string='Programmes/Options')
#
# class SchoolProgram(models.Model):
#     _name = 'school.program'
#     _description = 'Programme'
#
#     name = fields.Char(string='Nom', required=True)
#     total_hours = fields.Integer(string='Nombre d\'heures', compute='_compute_total_hours')
#     course_ids = fields.Many2many('school.course', string='Cours inclus')
#
#     @api.depends('course_ids')
#     def _compute_total_hours(self):
#         for program in self:
#             program.total_hours = sum(course.hours for course in program.course_ids)


