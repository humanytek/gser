from odoo import fields, models, api

class FlotaSerrano(models.Model):

    _inherit = "fleet.vehicle"
                    
    tipo_vehiculo = fields.Char(
        string="Tipo de vehiculo",
    )
    no_economico = fields.Char(
        string="No. economico",
    )
    #Parte del motor
    capacidad_tanque =fields.Integer(
        string="Capacidad del Tanque",
    )
    #Parte de modelo
    vig_poliza =fields.Date(
        string="Vigencia de la poliza",
    ) 
    file_poliza = fields.Binary(
        string="Carga Poliza",
    )

