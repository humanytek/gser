from odoo import fields, models, api
from odoo.exceptions import UserError

class button_ubicalo (models.Model):
    _inherit = 'fleet.vehicle'
    
    def button_ubicalo (self):
        return {
            'type' : 'ir.actions.act_url',
            'url' : '/endpoint/ubicalo'
        }
        # https://www.google.com/maps