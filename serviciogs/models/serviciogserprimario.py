from odoo import fields, models, api

class servicioGSerprimario (models.Model):

    _inherit = ['project.task']
    allow_timesheets=fields.Boolean(
        default = False,
    )
    contacto_facturacion = fields.Char(
        #comodel_name='res.partner',
        #ondelete='set null',
        #index=True,
        string="Contacto Facturación",
    )
    