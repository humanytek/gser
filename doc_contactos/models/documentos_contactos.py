from odoo import fields, models

class datosEmpleados (models.Model):
    _inherit="res.partner"
    #Documentacion personal
    estado_cuenta = fields.Binary(
        string="Caratula de estado de cuenta",
    )
    comprobante_domicilio = fields.Binary(
        string="Comp. Domicilio",
    )
    rfc = fields.Binary(
        string="RFC",
    )
    acta_constitutiva = fields.Binary(
        string="Acta constitutiva",
    )
    ine_representante = fields.Binary(
        string="INE representante legal",
    )
    otro = fields.Binary(
        string="Otro",
    )
    descripcion = fields.Binary(
        string="Descripcion",
    )
    #Fernando 2023
    f_licencia = fields.Date(
        string="Vigencia de licencia",
    )

    doc_f_licencia = fields.Binary(
        string="Licencia",
    )