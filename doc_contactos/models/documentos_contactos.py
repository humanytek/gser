from odoo import fields, models

class datosEmpleados (models.Model):
    _inherit="res.partner"
    #Documentacion personal
    estado_cuenta = fields.Binary(
        string="Caratula de estado de cuenta",
        #groups="hr.group_hr_user",
    )
    comprobante_domicilio = fields.Binary(
        string="Comp. Domicilio",
        #groups="hr.group_hr_user",
    )
    rfc = fields.Binary(
        string="RFC",
        #groups="hr.group_hr_user",
    )
    acta_constitutiva = fields.Binary(
        string="Acta constitutiva",
        #groups="hr.group_hr_user",
    )
    ine_representante = fields.Binary(
        string="INE representante legal",
        #groups="hr.group_hr_user",
    )
    otro = fields.Binary(
        string="Otro",
        #groups="hr.group_hr_user",
    )
    descripcion = fields.Binary(
        string="Descripcion",
        #groups="hr.group_hr_user",
    )
    