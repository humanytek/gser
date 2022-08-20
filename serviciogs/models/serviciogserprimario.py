from odoo import fields, models, api

class servicioGSerprimario (models.Model):

    _inherit = ['project.task']
   
    ejemplo = fields.Char(
        #comodel_name='res.partner',
        #ondelete='set null',
        #index=True,
        string="Contacto Facturación",
    )
    