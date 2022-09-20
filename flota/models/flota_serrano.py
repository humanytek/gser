
from odoo import fields, models, api

class FlotaSerrano(models.Model):

    _inherit = "fleet.vehicle"
                    
    tipo_vehiculo = fields.Selection([
        ('1','Unidad'),
        ('2','Remolque'),],
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
    num_poliza =fields.Char(
        string="Numero de poliza",
    )
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
    file_circulacion = fields.Binary(
        string ="Carga Circulación",
    )
    file_factura = fields.Binary(
        string= "Carga de Factura",
    )
   