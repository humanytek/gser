from odoo import fields, models, api

class FlotaSerrano(models.Model):

    _inherit = "fleet.vehicle"
                    
    tipo_vehiculo = fields.Char(
        string="Tipo de vehiculo",
    )
    no_economico = fields.Char(
        string="No. economico",
    )
    empresa = fields.Many2one(
        comodel_name='res.company',
        ondelete='set null',
        index=True,
    )