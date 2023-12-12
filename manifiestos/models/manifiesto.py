from odoo import models, fields, api

class Manifiesto(models.Model):
    _name = 'manifiestos.manifiesto'
    _description = 'Manifiesto de residuos'

    name = fields.Char(string='Numero de Manifiesto', compute='_compute_name', store=True)

    num_mani = fields.Char(string='Numero de Registro', required=True)
    instrucciones = fields.Char(string='Instrucciones de residuo', required=True)

    nombre_7 = fields.Char(string='Nombre y Firma', required=True)
    ruta = fields.Char(string='Ruta de la empresa', required=True)

    partner_id = fields.Many2one('res.partner', string='Cliente')
    emp_tralisol = fields.Selection([
        ('opc1', 'TRANSPORTADORA TRALISOL'),
        ('opc2', 'Traretesa, S.A. de C.V.'),
    ], string='Transporte/Empresa', required=True)

    emp_domicilio = fields.Selection([
        ('opc1', 'Carretera al Puesto km6, Centro, Lagos de Moreno, Jalisco. MEX CP 47400'),
        ('opc2', 'C. Porfirio Díaz No. 15, Col. Chichimeco, C. P. 47750, Atotonilco El Alto'),
    ], string='Transporte/Dirección', required=True)

    emp_telefono = fields.Char(string='Transporte/Telefono', required=True, default='(331)0310309')

    emp_permiso = fields.Selection([
        ('opc1', 'IMADES 393/2022'),
        ('opc2', 'DR 0817/18'),
        ('opc3', 'IRA-PRME-059/2009'),
        ('opc4', 'SSMAA-GIR-RT-665-22'),
        ('opc5', 'ERRME-12-22'),
        ('opc6', 'DR 0759/18'),
    ], string='Permiso Gobierno', required=True)

    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehículo')
    fecha_1 = fields.Date(string='Fecha de embarque')

    contact_id = fields.Many2one('res.partner', string='Contacto')
    num_autorizacion = fields.Selection([
        ('opc1', 'DREMI1405300046/CA/CO/RE/18'),
        ('opc2', 'DEMI1409800691/CA/17'),
        ('opc3', 'DEMI1405301078/CO/'),
        ('opc4', 'IMADES DGA.PS. 009/2023'),
    ], string='Numero autorización', required=True)

    des_nombre = fields.Selection([
        ('opc1', 'Eduardo Ernesto Serrano Serrano/ P.A. Olivia Eunice Osornio Macias'),
        ('opc2', 'Guillermo Chaim Serrano'),
        ('opc3', 'Maricela Contreras'),
    ], string='Nombre destinatario')

    cargo = fields.Selection([
        ('opc1', 'Representante Técnico'),
        ('opc2', 'Representante Legal'),
        ('opc3', 'Coordinadora de Operaciones'),
    ], string='Cargo')

    fecha_2 = fields.Date(string='Fecha de recepción')

    lines = fields.One2many('manifiestos.line', 'manifiesto_id', string='Líneas de facturación')

    def generate_qr_code_text(self):
        emp_tralisol_display = dict(self._fields['emp_tralisol'].selection).get(self.emp_tralisol, 'Valor Desconocido')
        qr_text = f"Fecha: {self.fecha_2}, Folio: {self.name}, Cliente: {self.partner_id.name}, Proveedor: {emp_tralisol_display}"
        return qr_text

    estado = fields.Selection([
        ('ags', 'Aguascalientes'),
        ('gto', 'Guanajuato'),
        ('jal', 'Jalisco'),
        ('nay', 'Nayarit'),
        ('col', 'Colima'),
    ], string='Estado', required=True)

    consecutivo = fields.Char(string='Consecutivo', compute='_compute_consecutivo', store=True)

    @api.depends('estado')
    def _compute_consecutivo(self):
        for record in self:
            if record.estado:
                # Puedes definir una lógica personalizada para generar el consecutivo
                if record.estado == 'ags':
                    prefix = 'AGS'
                elif record.estado == 'gto':
                    prefix = 'GTO'
                elif record.estado == 'jal':
                    prefix = 'JAL'
                elif record.estado == 'nay':
                    prefix = 'NAY'
                elif record.estado == 'col':
                    prefix = 'COL'

                # Consulta la base de datos para contar registros existentes con el mismo estado
                consecutivo = self.env['manifiestos.manifiesto'].search_count([('estado', '=', record.estado)])

                # Formatea el consecutivo con un prefijo y ceros a la izquierda
                record.consecutivo = f'{prefix}-{consecutivo + 1:06d}'
            else:
                record.consecutivo = False
    
    @api.depends('consecutivo')
    def _compute_name(self):
        for record in self:
            # Establece el campo "name" igual al campo "consecutivo"
            record.name = record.consecutivo


class ManifiestoLine(models.Model):
    _name = 'manifiestos.line'
    _description = 'Línea de facturación del manifiesto'

    manifiesto_id = fields.Many2one('manifiestos.manifiesto', string='Manifiesto')
    product_id = fields.Many2one('product.product', string='Producto')
    tipo = fields.Char(string='Tipo')
    cantidad = fields.Float(string='Cantidad')
    capacidad = fields.Float(string='Capacidad')
    unidad = fields.Char(string='Unidad')
    clasifi_gto = fields.Selection([
        ('opc1', 'No aplica'),
        ('opc2', 'RR'),
        ('opc3', 'RNV'),
    ], string='CLASIFICACIÓN', default='opc1')


class ManifiestoReport(models.AbstractModel):

    _name='report.manifiestos.report_manifiesto_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('manifiestos.report_manifiesto_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['manifiestos.manifiesto'],
            'docs': self.env['manifiestos.manifiesto'].browse(docids)
        }

