from odoo import fields, models

class clientescampos (models.Model):
    _inherit="res.partner"
    #Documentacion personal

    street_name = fields.Char(required=True)
    street_number = fields.Char(required=True)
    street_number2 = fields.Char(required=True)
    city = fields.Char(required=True)
    state_id = fields.Many2one('res.country.state', string='State', required=True)
    zip = fields.Char(required=True)
    country_id = fields.Many2one('res.country', string='Country', required=True)
    mobile = fields.Char(required=True)
    email = fields.Char(required=True)
    ine_representante = fields.Binary(required=True)         
