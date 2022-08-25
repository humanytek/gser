import string
from odoo import fields, models, api

class servicioGSerprimario (models.Model):
    _inherit = ['project.task']

    #@api.multi
    #def name_get(self):
    #    res = []
    #    for rec in self:
    #        res.append((rec.model_id, '%s - %s' % (rec.no_economico, rec.license_plate)))
    #        #res.append((rec.model_id, '%s - %s' % (rec.no_economico, rec.license_plate)))
    #    return res

    status_viaje = fields.Selection([
        ('1','Programado'),
        ('2','Pendiente de gastos'),
        ('3','Pendiente de diesel'),
        ('4','Pendiente de carta porte'),
        ('5','En trayecto'),
        ('6','En validación'),
        ('7','Por facturar'),
        ('8','Por cobrar'),
        ('8','Finalizado'),
        ('8','Cancelado'),
        ('8','Rechazado'),],
        string="Estado de Viaje",
    )
    vehiculo = fields.Many2one(
        comodel_name='fleet.vehicle',
        ondelete='set null',
        index=True,
        string="Vehiculo",
    )
    anio_vehiculo = fields.Char(
        related ='vehiculo.model_year',
        string="Año vehículo",
    )
   
    remolque_1 = fields.Many2one(
        comodel_name ='fleet.vehicle',
        ondelete ='set null',
        index=True,
        string="Remolque 1",
    )
    remolque_2 = fields.Char(
        related ='remolque_1.no_economico',
        strore=True,
        string="No. Economico Remolque",
    )
    remolque = fields.Many2one(
        comodel_name ='project.project',
        ondelete ='set null',
        index=True,
        string="Remolque 1",
    )
    tipo_ruta_viaje= fields.Char(
        related ='remolque.tipo_ruta',
        string ="Tipo Ruta",
    )
    carga_viaje= fields.Char(
        string ="",
    )  
    capacidad_viaje = fields.Char(
        string ="",
    ) 
    producto_viaje = fields.Char(
        string ="",
    ) 
    conductor = fields.Char(
        string ="",
    )  
    gasto_total_op_viaje= fields.Char(
        string ="",
    )
    gasto_total_caseta_viaje= fields.Char(
        string ="",
    )   
    disel_viaje= fields.Char(
        string ="",
    )   
    km_viaje= fields.Char(
        string ="",
    )   
    carga_combustible= fields.Char(
        string ="",
    )