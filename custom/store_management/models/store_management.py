from odoo import models, fields

class StoreManagement(models.Model):
    _name = 'store' #### nom hyper important, sera appellé par le views et le csv
    _description = 'Module Général de gestion des magasins'

    name= fields.Char(string="Nom du magasin") ### ajouter un required = true dans la view
    contact= fields.Many2one('res.partner' ,string='Contact')
    telephone=fields.Char(related='contact.phone',string="Numéro de téléphone")
    sale_revenue=fields.Float(string="Chiffre d'affaire") ## invisible dans view tree
    number_of_employees=fields.Integer(string="Nombre d'employés")## invisible dans view tree
    image = fields.Image(related='contact.image_1920',string="Image") ## invisible dans view tree