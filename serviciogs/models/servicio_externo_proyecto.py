from email.policy import default
from unittest.mock import DEFAULT
from odoo import fields, models, api
from datetime import date
from datetime import datetime
from datetime import timedelta

class servicio_externo_proyecto (models.Model):
    _inherit = ['project.task']
    allow_timesheets=fields.Boolean(
        default = False,
    )   
    estatus_viaje = fields.Selection([
        ('1','Programado'),
        ('2','Pendiente de gastos'),
        ('3','Pendiente de diesel'),
        ('4','Pendiente de carta porte'),
        ('5','En trayecto'),
        ('6','En validación'),
        ('7','Por facturar'),
        ('8','Por cobrar'),
        ('9','Finalizado'),
        ('10','Cancelado'),
        ('12','Rechazado'),],
        string="Estatus de Viaje",
        default='1',
    )
    vehiculo = fields.Many2one(
        comodel_name='fleet.vehicle',
        #compute = 'compute_vihicle',
        #ondelete='set null',
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
    r1_no_economico = fields.Char(
        related ='remolque_1.no_economico',
        string="No. Economico r1",
    )
    remolque_2 = fields.Many2one(
        comodel_name ='fleet.vehicle',
        ondelete ='set null',
        index=True,
        string="Remolque 2",
    )
    r2_no_economico = fields.Char(
        related ='remolque_2.no_economico',
        string="No. Economico r2",
    )
    tipo_ruta_viaje= fields.Selection(
       related = 'project_id.tipo_precio',
        string ="Tipo Ruta",
    )
    carga_viaje= fields.Selection(
        related = 'project_id.carga_ruta',
        string ="Carga",
    )
    capacidad_viaje = fields.Selection(
        related ='project_id.capacidad_ruta',
        string ="Capacidad",
    )
    producto_viaje = fields.Many2one(
        related ='project_id.producto_ruta',
        string ="Producto",
    )
    conductor = fields.Many2one(
        compute = '_compute_driver',
        related ='vehiculo.conductor',
        string ="Conductor",
    )
    gasto_total_op_viaje= fields.Float(
        related ='project_id.gasto_total_operador',
        string ="Gastos del operador",
    )

    #gasto_total_caseta_viaje= fields.Float(
    #    related ='project_id.caseta_efectivo',
    #    string ="Gasto total - caseta",
    #)
    gasto_total_caseta_viaje= fields.Float(
        compute ='_compute_gasto_total_caseta_viaje',
        string ="Gasto total - caseta",
    )   
    diesel_viaje= fields.Float(
        related ='project_id.diesel',
        string ="Diesel",
    )   
    km_viaje= fields.Float(
        related ='project_id.km_ruta',
        string ="Kilometraje",
    )   
    carga_combustible= fields.Selection([
        ('1','Grupo Serrano'),
        ('2','Gasolinera La Loma'),
        ('3','Otro'),],
        string="Carga de combustible",
    )
    pmanager = fields.Many2one(
        string ="Manager",
        comodel_name='res.users',
        default=lambda self: self.env.user.id
    )
    cantidad = fields.Float(
        string ="Cantidad",
    )          
    precio_ruta_litro = fields.Float(
        related ="project_id.precio",
        string ="Precio ruta / litro",
    )    
    subtotal   = fields.Float(
        compute='_compute_subtotal',
        string ="Subtotal",
    )     
    iva = fields.Float(
        compute='_compute_iva',
        string ="IVA 16%",
    )    
    retencion = fields.Float(
        compute ='_compute_retencion',
        string ="Retención 4%",
    )   
    total_facturar = fields.Float(
        compute ='_compute_total_facturar',
        string ="Total a Facturar",
        store=True,
    )
    forma_pago = fields.Selection([
        ('1','Transferencia'),
        ('2','Efectivo'),],
        string ="Forma de pago",
    )
    no_factura = fields.Many2one(
        comodel_name='account.move',
        ondelete='set null',
        index=True,
        string ="No. Factura",
    )          
    #no_factura = fields.Char(
        #comodel_name='account.move',
        #ondelete='set null',
        #index=True,
        #string ="No. Factura",
    #)    
    fecha_factura = fields.Date(
        string ="Fecha de factura",
    )
    fecha_pago = fields.Date(
        string ="Fecha pago",
    )
    
    con_retencion = fields.Selection([
        ('0','SI'),
        ('1','NO'),],
        string ="Con Retencion",
        default ='0',
    )
    caseta_llave_1 = fields.Float(
        related ="project_id.caseta_llave",
        string ="Caseta IAVE",
    )
    caseta_efectivo_1 = fields.Float(
        related ="project_id.caseta_efectivo",
        string ="Caseta Efectivo",
    )    
    
    @api.depends("cantidad", "precio_ruta_litro")
    def _compute_subtotal(self):
        for record in self:
            record.subtotal = record.cantidad * record.precio_ruta_litro
    @api.depends("subtotal")
    def _compute_iva(self):
        for record in self:
            record.iva = record.subtotal * 0.16
    @api.depends("con_retencion","subtotal")
    def _compute_retencion(self):
        for record in self:
            if record.con_retencion == '1':
                record.retencion = 0
            else:
                record.retencion = record.subtotal * 0.04
    @api.depends("subtotal", "iva", "retencion", "cantidad", "total_facturar")
    def _compute_total_facturar(self):
        for record in self:
            if record.total_facturar != 0:
                record.total_facturar = record.total_facturar
            else:
                record.total_facturar = (record.subtotal + record.iva) - record.retencion
            if record.cantidad == 0:
                record.total_facturar = 0

    @api.depends('project_id.caseta_efectivo', 'project_id.caseta_llave')
    def _compute_gasto_total_caseta_viaje(self):
        for record in self:
            record.gasto_total_caseta_viaje = record.project_id.caseta_efectivo + record.project_id.caseta_llave
            
    @api.onchange('vehiculo')
    def _compute_driver(self):
        if self.vehiculo:
            if not self.vehiculo.conductor:
                warning = {
                        'title': 'Conductor no registrado. ',
                        'message': 'El Vehiculo "%s" con placas : "%s"  no posee conductor registrado \nPor favor registrarlo.' % (self.vehiculo.model_id.name, self.vehiculo.license_plate,),
                        #'type': 'notification',
                }
                self.update({
                    'vehiculo': False,})
                return {'warning': warning}
            elif self.vehiculo.conductor:
                #LICENCIA
                if not self.vehiculo.conductor.vigencia or not self.vehiculo.conductor.licencia:
                    warning = {
                        'title': 'Registrar documento. ',
                        'message': 'El conductor %s relacionado al vehiculo "%s" con placas : "%s" , no posee Licencia registrada \nPor favor cargar documento y registrar la respectiva fecha de vigencia.' % (self.vehiculo.conductor.name, self.vehiculo.model_id.name, self.vehiculo.license_plate,),
                        #'type': 'notification',
                    }
                    self.update({
                        'vehiculo': False,})
                    return {'warning': warning}
                elif self.vehiculo.conductor.vigencia:
                    now = datetime.now()
                    now = datetime.date(now)
                    expiration_date = self.vehiculo.conductor.vigencia
                    warning_date = self.vehiculo.conductor.vigencia - timedelta(days = 30 )
                    if now > expiration_date:
                        warning = {
                            'title': 'Licencia vencida.',
                            'message': 'El conductor %s relacionado al vehiculo "%s" con placas : "%s"  \nPosee vencida su LICENCIA, verificar el respectivo proceder.' % (self.vehiculo.conductor.name, self.vehiculo.model_id.name, self.vehiculo.license_plate,),
                            #'type': 'notification',
                        }
                        self.update({
                        'vehiculo': False,})
                        return {'warning': warning}
                    #Licencia por vencer
                    # elif expiration_date >= now and warning_date <= now:
                    #     exp_days = now - expiration_date
                    #     exp_days = str(exp_days).replace("-", "").replace(" 0:00:00", "").replace("day,", "").replace("days,", "")
                    #     warning = {
                    #             'title': 'Documento por Vencer.',
                    #             'message': 'El conductor %s relacionado al vehiculo "%s" con placas : "%s"  \nTiene %s dia(s) previo(s) al vencimiento de su Licencia.' % (self.vehiculo.conductor.name, self.vehiculo.model_id.name, self.vehiculo.license_plate, exp_days),
                    #             #'type': 'notification',
                    #     }
                    #     return {'warning': warning,}
                    
                    
            #POLIZA
            if not self.vehiculo.vigencia_poliza or not self.vehiculo.file_poliza:
                warning = {
                    'title': 'Registrar Poliza. ',
                    'message': 'El Vehiculo  %s  con Placa :  %s no registra Poliza. \nPor favor cargar documento y registrar la respectiva fecha de vigencia.' % (self.vehiculo.model_id.name, self.vehiculo.license_plate,),
                    #'type': 'notification',
                }
                self.update({
                'vehiculo': False,})
                return {'warning': warning}
                                
            elif self.vehiculo.vigencia_poliza:
                now = datetime.now()
                now = datetime.date(now)
                expiration_date = self.vehiculo.vigencia_poliza
                warning_date = self.vehiculo.vigencia_poliza - timedelta(days = 30 )
                if now > expiration_date:
                    warning = {
                        'title': 'Poliza vencida.',
                        'message': 'El Vehiculo seleccionado "%s" con Placa : %s \nTiene vencida su poliza, por favor actualizar la vigencia.' % (self.vehiculo.model_id.name, self.vehiculo.license_plate),
                        #'type': 'notification',
                    }
                    return {'warning': warning}
                # elif expiration_date >= now and warning_date <= now:
                #     exp_days = now - expiration_date
                #     exp_days = str(exp_days).replace("-", "").replace(" 0:00:00", "").replace("day,", "").replace("days,", "")
                #     warning = {
                #             'title': 'Documento por Vencer.',
                #             'message': 'El Vehiculo "%s"  con Placa : %s \nTiene poliza vigente  %s dia(s) , Actualizarla en la brevedad posible.' % (self.vehiculo.model_id.name, self.vehiculo.license_plate, exp_days),
                #             #'type': 'notification',
                #     }
                #     return {'warning': warning}
                    
            #EXAMEN DE CONDUCCION        
            if not self.vehiculo.conductor.vigencia_exam or not self.vehiculo.conductor.chofer_examen:
                warning = {
                'title': 'Registrar Examen . ',
                'message': 'El conductor %s relacionado al vehiculo "%s" con placas "%s" no registra examen \nPor favor cargar documento y registrar la respectiva fecha de vigencia.' % (self.vehiculo.conductor.name, self.vehiculo.model_id.name, self.vehiculo.license_plate),
                #'type': 'notification',
                }
                self.update({
                    'vehiculo': False,})
                return {'warning': warning}
            elif self.vehiculo.conductor.vigencia_exam:
                now = datetime.now()
                now = datetime.date(now)
                expiration_date = self.vehiculo.conductor.vigencia_exam
                warning_date = self.vehiculo.conductor.vigencia_exam - timedelta(days = 30 )
                if now > expiration_date:
                    warning = {
                        'title': 'Examen vencida.',
                        'message': 'El conductor %s relacionado al vehiculo "%s" con placas "%s tiene vencido su examen de conduccion. \nPor favor verificar el respectivo proceder.' % (self.vehiculo.conductor.name, self.vehiculo.model_id.name, self.vehiculo.license_plate),
                        #'type': 'notification',
                    }
                    self.update({
                    'vehiculo': False,})
                    return {'warning': warning}
                # elif expiration_date >= now and warning_date <= now:
                #     exp_days = now - expiration_date
                #     exp_days = str(exp_days).replace("-", "").replace(" 0:00:00", "").replace("day,", "").replace("days,", "")
                #     warning = {
                #             'title': 'Documento por Vencer.',
                #             'message': 'El conductor %s  \n Tiene %s dias habiles, antes de que venza la vigencia de su examen de conduccion, por favor verificar el respectivo proceder.' % (self.vehiculo.conductor.name, exp_days),
                #             #'type': 'notification',
                #     }
                #     return {'warning': warning}
                
                
                
                
            #FISICO MECANICO  
            if not self.vehiculo.vigencia_fisico_mecanico or not self.vehiculo.file_fisico_mecanico:
                warning = {
                    'title': 'Registrar Fisico Mecanica  . ',
                    'message': 'El Vehiculo  %s  con Placa :  %s \nNo registra Fisico Mecanico \nPor favor cargar documento y registrar la respectiva fecha de vigencia.' % (self.vehiculo.model_id.name, self.vehiculo.license_plate,),
                    #'type': 'notification',
                }
                self.update({
                        'vehiculo': False,})
                return {'warning': warning}    
            elif self.vehiculo.vigencia_fisico_mecanico:
                now = datetime.now()
                now = datetime.date(now)
                expiration_date = self.vehiculo.vigencia_fisico_mecanico
                warning_date = self.vehiculo.vigencia_fisico_mecanico - timedelta(days = 30 )
                if now > expiration_date:
                    warning = {
                        'title': 'Fecha Fisico Mecanica vencida.',
                        'message': 'El Vehiculo seleccionado %s con Placa : %s \nTiene vencida la vigencia F/M, por favor verificar el respectivo proceder.' % (self.vehiculo.model_id.name, self.vehiculo.license_plate),
                        #'type': 'notification',
                    }
                    self.update({
                        'vehiculo': False,})
                    return {'warning': warning}
                # elif expiration_date >= now and warning_date <= now:
                #     exp_days = now - expiration_date
                #     exp_days = str(exp_days).replace("-", "").replace(" 0:00:00", "").replace("day,", "").replace("days,", "")
                #     warning = {
                #             'title': 'Documento por Vencer.',
                #             'message': 'El Vehiculo %s  con Placa : %s \nTiene el documento Fisico Mecanica  %s dias habiles , por favor regularizar y verificar el respectivo proceder..' % (self.vehiculo.model_id.name, self.vehiculo.license_plate, exp_days),
                #             #'type': 'notification',
                #     }
                #     return {'warning': warning}
                
                
            #EMISION  
            if not self.vehiculo.vigencia_emisiones or not self.vehiculo.file_emisiones:
                warning = {
                    'title': 'Registrar Emisiones. ',
                    'message': 'El Vehiculo  %s  con Placa :  %s \nNo registra Emisiones \nPor favor cargar documento y registrar la respectiva fecha de vigencia.' % (self.vehiculo.model_id.name, self.vehiculo.license_plate,),
                    #'type': 'notification',
                }
                self.update({
                        'vehiculo': False,})
                return {'warning': warning}    
            elif self.vehiculo.vigencia_emisiones:
                now = datetime.now()
                now = datetime.date(now)
                expiration_date = self.vehiculo.vigencia_emisiones
                warning_date = self.vehiculo.vigencia_emisiones - timedelta(days = 30 )
                if now > expiration_date:
                    warning = {
                        'title': 'Emisiones vencida.',
                        'message': 'El Vehiculo seleccionado %s con Placa : %s \nTiene vencida la vigencia de emisiones, por favor verificar el respectivo proceder.' % (self.vehiculo.model_id.name, self.vehiculo.license_plate),
                        #'type': 'notification',
                    }
                    self.update({
                        'vehiculo': False,})
                    return {'warning': warning}
                
                    
                    #####################***VIGENCIA***##############################           
                    
            if self.vehiculo.conductor.vigencia:
                now = datetime.now()
                now = datetime.date(now)
                expiration_date = self.vehiculo.conductor.vigencia
                warning_date = self.vehiculo.conductor.vigencia - timedelta(days = 30 )
                #Licencia vencida
                if expiration_date >= now and warning_date <= now:
                    exp_days = now - expiration_date
                    exp_days = str(exp_days).replace("-", "").replace(" 0:00:00", "").replace("day,", "").replace("days,", "")
                    warning = {
                            'title': 'Documento por Vencer.',
                            'message': 'El conductor %s relacionado al vehiculo "%s" con placas : "%s"  \nTiene %s dia(s) previo(s) al vencimiento de su Licencia.' % (self.vehiculo.conductor.name, self.vehiculo.model_id.name, self.vehiculo.license_plate, exp_days),
                            #'type': 'notification',
                    }
                    return {'warning': warning,}                
                    
            if self.vehiculo.vigencia_poliza:
                now = datetime.now()
                now = datetime.date(now)
                expiration_date = self.vehiculo.vigencia_poliza
                warning_date = self.vehiculo.vigencia_poliza - timedelta(days = 30 )
                if expiration_date >= now and warning_date <= now:
                    exp_days = now - expiration_date
                    exp_days = str(exp_days).replace("-", "").replace(" 0:00:00", "").replace("day,", "").replace("days,", "")
                    warning = {
                            'title': 'Documento por Vencer.',
                            'message': 'El Vehiculo "%s"  con Placa : %s \nTiene poliza vigente  %s dia(s) , Actualizarla en la brevedad posible.' % (self.vehiculo.model_id.name, self.vehiculo.license_plate, exp_days),
                            #'type': 'notification',
                    }
                    return {'warning': warning}
                
            if self.vehiculo.conductor.vigencia_exam:
                now = datetime.now()
                now = datetime.date(now)
                expiration_date = self.vehiculo.conductor.vigencia_exam
                warning_date = self.vehiculo.conductor.vigencia_exam - timedelta(days = 30 )
                if expiration_date >= now and warning_date <= now:
                    exp_days = now - expiration_date
                    exp_days = str(exp_days).replace("-", "").replace(" 0:00:00", "").replace("day,", "").replace("days,", "")
                    warning = {
                            'title': 'Documento por Vencer.',
                            'message': 'El conductor %s  \n Tiene %s dias habiles, antes de que venza la vigencia de su examen de conduccion, por favor verificar el respectivo proceder.' % (self.vehiculo.conductor.name, exp_days),
                            #'type': 'notification',
                    }
                    return {'warning': warning}
            
            if self.vehiculo.vigencia_fisico_mecanico:
                now = datetime.now()
                now = datetime.date(now)
                expiration_date = self.vehiculo.vigencia_fisico_mecanico
                warning_date = self.vehiculo.vigencia_fisico_mecanico - timedelta(days = 30 )
                if expiration_date >= now and warning_date <= now:
                    exp_days = now - expiration_date
                    exp_days = str(exp_days).replace("-", "").replace(" 0:00:00", "").replace("day,", "").replace("days,", "")
                    warning = {
                            'title': 'Documento por Vencer.',
                            'message': 'El Vehiculo %s  con Placa : %s \nTiene el documento Fisico Mecanica  %s dias habiles , por favor regularizar y verificar el respectivo proceder..' % (self.vehiculo.model_id.name, self.vehiculo.license_plate, exp_days),
                            #'type': 'notification',
                    }
                    return {'warning': warning}
                
            if self.vehiculo.vigencia_emisiones:
                now = datetime.now()
                now = datetime.date(now)
                expiration_date = self.vehiculo.vigencia_emisiones
                warning_date = self.vehiculo.vigencia_emisiones - timedelta(days = 30 )
                if expiration_date >= now and warning_date <= now:
                    exp_days = now - expiration_date
                    exp_days = str(exp_days).replace("-", "").replace(" 0:00:00", "").replace("day,", "").replace("days,", "")
                    warning = {
                            'title': 'Documento por Vencer.',
                            'message': 'El Vehiculo %s  con Placa : %s \nTiene el documento emisiones  %s dias habiles , por favor regularizar y verificar el respectivo proceder..' % (self.vehiculo.model_id.name, self.vehiculo.license_plate, exp_days),
                            #'type': 'notification',
                    }
                    return {'warning': warning}
