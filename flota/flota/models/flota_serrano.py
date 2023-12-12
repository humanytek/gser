from odoo import fields, models, api

class FlotaSerrano(models.Model):
    _inherit = "fleet.vehicle"                 
    tipo_vehiculo = fields.Selection([
        ('1','Tractocamion'),
        ('2','Torton'),
        ('3','Pickup'),
        ('4','Unidad'),
        ('5','Maquinaria Pesada'),
        ('6','Volteo'),
        ('7','Tanque'),
        ('8','Caja Seca'),
        ('9','Gondola'),
        ('10','Plataforma'),
        ('11','Cama Baja'),
        ('12','Caja Refrigerada'),
        ('13','Tanque de Acero Inoxidable'),
        ('14','Plana'), 
        ('15','Remolque'),
        ('16','Torton Roll Off'),],
        string="Tipo de vehiculo",
    )
    no_economico = fields.Char(
        string="No. economico",
    )   
    capacidad_remolque = fields.Char(
        string="Capacidad Remolque",
    )
    #Parte del motor
    capacidad_tanque =fields.Integer(
        string="Capacidad del Tanque",
    )
    #Parte de modelo
    numero_poliza =fields.Char(
        string="Numero de poliza",
    )
    vigencia_poliza =fields.Date(
        string="Vig. de la poliza",
    ) 
    file_poliza = fields.Binary(
        string="Carga Poliza",
    )
    vigencia_fisico_mecanico =fields.Date(
        string="Vig. Fisico-Mecanico",
    ) 
    file_fisico_mecanico = fields.Binary(
        string="Carga Poliza F-Mecanico",
    )
    vigencia_emisiones =fields.Date(
        string="Vig.Emisiones",
    ) 
    file_emisiones = fields.Binary(
        string="Carga Emisiones",
    )
    file_circulacion = fields.Binary(
        string ="Carga Circulación",
    )
    file_factura = fields.Binary(
        string= "Carga de Factura",
    )
    file_otro = fields.Binary(
        string= "Otro",
    )
    conductor = fields.Many2one(
        comodel_name='hr.employee',
        ondelete='set null',
        index=True,
        string="Conductor",
    )