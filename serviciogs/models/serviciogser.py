from odoo import fields, models, api

class servicioGSer (models.Model):
    _inherit="project.project"
    _inherit="sale.order"
    status_ruta = fields.Selection([
        ('1','Activa'),
        ('2','Inactiva'),],
        string="Estatus Ruta",
    )
    contacto_facturacion = fields.Char(
        string="Contacto Facturación",
    )
    email_facturacion = fields.Char(
        string="E-mail Facturación",
    )
    km_ruta = fields.Float(
        string="Kilometros",
    )
    carga_ruta = fields.Selection([
        ('1','Full'),
        ('2','Sencillo'),
        ('3','Caja seca'),
        ('4','Gondola'),
        ('5','Plataforma'),
        ('6','Torton'),
        ('7','N/A'),
        ('8','12'),],
        string="Carga",
    )
    capacidad_ruta = fields.Selection([
        ('1','25,000 Litros'),
        ('2','30,000 Litros'),
        ('3','35,000Litros'),
        ('4','36,000 Litros'),
        ('5','50,000 Litros'),
        ('6','54,000 Litros'),
        ('7','2 Tonelada'),
        ('8','10 Tonelada'),
        ('9','20 Tonelada'),
        ('10','30 Tonelada'),
        ('11','N/A'),],
        string="Capacidad",
    )
    ejes_ruta = fields.Selection([
        ('1','2 ejes'),
        ('2','3 ejes'),
        ('3','5 ejes'),
        ('4','6 ejes'),
        ('5','9 ejes'),],
        string="Ejes",
    )
    producto_ruta = fields.Selection([
        ('1','Aceite'),
        ('2','Aceite pollo'),
        ('3','Crema'),
        ('4','Cascarilla de arroz'),
        ('5','Leche'),
        ('6','Leche en polvo'),
        ('7','Lacteos'),
        ('8','Lodos planta tratamientos'),
        ('9','Pluma'),
        ('10','Refacciones'),
        ('11','Otros'),],
        string="Producto",
    )

    
    tipo_precio = fields.Selection([
        ('1','Ruta'),
        ('2','Litro'),
        ('3','Kilogramo'),],
        string="Tipo de precio",
    )
    precio = fields.Float(
        string="Precio",
    )
    precio_disel = fields.Float(
        default = 20.00,
        string="Precio Disel",
    )
    rendimiento = fields.Float(
        default=2.2,
        string="Rendimiento",
    )
    disel = fields.Float(
        compute='_compute_disel',
    )
    caseta_efectivo = fields.Float(
        string="Caseta Efectivo",
    )
    caseta_llave = fields.Float(
        string="Caseta Llave",
    )
    gasto_op = fields.Float(
        string="Gasto Operador",
    )
    gasto_totalOper = fields.Float(
        compute='_compute_gastoopera',
        string="Gasto Total del Operador",
    )
    gasto_total = fields.Float(
        compute='_compute_gastoT',
        string="Gasto Total",
    )
    
    #conductor = fields.Many2one(
    #    comodel_name='hr.employee',
    #    ondelete='set null',
    #    index=True,
    #)
   
    @api.depends("disel", "precio_disel","caseta_llave","gasto_op","caseta_efectivo")
    def _compute_gastoT(self):
        for record in self:
            record.gasto_total = (record.disel * record.precio_disel) + record.caseta_llave + record.caseta_efectivo + record.gasto_op

    @api.depends("caseta_efectivo", "gasto_op")
    def _compute_gastoopera(self):
        for record in self:
            record.gasto_totalOper = record.caseta_efectivo + record.gasto_op

    @api.depends("km_ruta", "rendimiento")
    def _compute_disel(self):
        for record in self:
            record.disel = record.km_ruta / record.rendimiento

class servicioGSerVenta (models.Model):
    _inherit="sale.order"
    ord_vent = fields.Char(
        string="Orden de venta",
    )
    @api.onchange('partner_id')
    def onchangue_or_venta(self):
        self.ord_vent = self.partner_id.name
