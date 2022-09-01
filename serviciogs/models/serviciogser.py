from odoo import fields, models, api

class servicioGSer (models.Model):
    # Hacemos referencia al modelo al cual vamos a heredar.
    _inherit = ['project.project']

    # Desabilihitar la parte de las hojas de trabajo
    allow_timesheets=fields.Boolean(
        default = False,
    )
# Campos agregados al modelo de proyecto seccion principal
    status_ruta = fields.Selection([
        ('1','Activa'),
        ('2','Inactiva'),],
        string="Estatus Ruta",
    )
    # Campos relacional de muchos a uno
    # comodel_name, se hace referencia al modelo a utilizar
    #
    #index =  True indica que lo va a indexar a la BD.
    #string es nuestro label del campo
    contacto_facturacion = fields.Many2one(
        comodel_name='res.partner',
        ondelete='set null',
        index=True,
        string="Contacto Facturación",
    )
    #COD-GSer-001# Campo con un related
    #El tipo de dato debe ser Char para poder realizar la extración de un campo relacionado
    #Debe existir un campo ya con una relacion efectuada.
    #se agrega palabra reservada "related" la cual 
    email_facturacion = fields.Char(
        related ='contacto_facturacion.email',
        string="E-mail Facturación",
    )
    ord_vent = fields.Many2one(
        comodel_name='sale.order',
        ondelete='set null',
        index=True,
        string="Orden de Venta",
    )
    
#Campos de la sección de Ruta.Ruta


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

    #ord_vent = fields.Many2one(
    #    comodel_name='sale.order',
    #    ondelete='set null',
    #    index=True,
    #)
    tipo_precio = fields.Selection([
        ('1','Ruta'),
        ('2','Litro'),
        ('3','Kilogramo')],
        string="Tipo de precio",
        index = True,
    )
   
    precio = fields.Float(
        string="Precio",
    )
    precio_disel = fields.Float(
        default = 20.00,
        string="Precio Diesel",
    )
    rendimiento = fields.Float(
        default=2.2,
        string="Rendimiento",
    )
    disel = fields.Float(
        compute='_compute_disel',
        string ='Diesel'
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
    
    recogen = fields.Char(
        string="Se recoge en:",
    )
    direccion_or= fields.Char(
        string="Dirección origen:",
    )
    pais_or= fields.Many2one(
        string ="País origen:",
        comodel_name='res.country',
        ondelete='set null',
        index=True,
    )
    estado_or= fields.Many2one(
        string ="Estado origen:",
        comodel_name='res.country.state',
        ondelete='set null',
        index=True,
    )
    ciudad_or= fields.Char(
        string ="Ciudad origen:",
        comodel_name='res.city',
        ondelete='set null',
        index=True,
    )
    entregaD = fields.Char(
        string="Se entrega en:",
    )
    direccion_des= fields.Char(
        string="Dirección destino:",
    )
    pais_des= fields.Many2one(
        string ="País destino:",
        comodel_name='res.country',
        ondelete='set null',
        index=True,
    )
    estado_des= fields.Many2one(
        string ="Estado destino:",
        comodel_name='res.country.state',
        ondelete='set null',
        index=True,
    )
    ciudad_des= fields.Char(
        string ="Ciudad destino:",
        #comodel_name='res.country.city',
        #ondelete='set null',
        #index=True,
    )
   
    #@api.onchange('partner_id')
    #def onchangue_ordventas(self):
    #    self.ord_vent = self.partner_id

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

    