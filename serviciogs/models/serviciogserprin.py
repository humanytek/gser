from odoo import fields, models, api

class servicioGSerPrincipal (models.Model):

    _inherit = ['project.task']

    n = fields.Selection([
        ('1','Activa'),
        ('2','Inactiva'),],
        string="Estatus Ruta",
    )
   
    
   