from odoo import fields, models, api

class FlotaSerrano(models.Model):

    _inherit = "fleet.vehicle"
                    
    tipo_vehiculo = fields.Selection([
        ('1','Tracto'),
        ('2','Tracto2'),],
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
        string="Vig. de la poliza",
    ) 
    file_poliza = fields.Binary(
        string="Carga Poliza",
    )
    vig_fm =fields.Date(
        string="Vig. Fisico-Mecanico",
    ) 
    file_fm = fields.Binary(
        string="Carga Poliza F-Mecanico",
    )
    vig_contamin =fields.Date(
        string="Vig.Emisiones",
    ) 
    file_contamin = fields.Binary(
        string="Carga Emisiones",
    )
    

