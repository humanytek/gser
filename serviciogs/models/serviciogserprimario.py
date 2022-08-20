from odoo import fields, models, api

class servicioGSerprimario (models.Model):

    _inherit = ['project.task']
   
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
        related ='model_id.model_year',
        string="Año vehículo",
    )

    