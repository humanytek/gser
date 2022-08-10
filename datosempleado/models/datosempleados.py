from odoo import fields, models

class datosEmpleados (models.Model):
    _inherit="hr.employee"
    domicilio = fields.Binary(
        string="Comp. Domicilio",
    )
    estudios = fields.Binary(
        string="Comp. Estudios",
    )
    imss = fields.Binary(
        string="IMSS",
    )
    infonavit = fields.Binary(
        string="Comp. Infonavit",
    )
    curp = fields.Binary(
        string='CURP',
    )
    rfc = fields.Binary(
        string='RFC',
    )
    ine = fields.Binary(
        string='INE',
    )
    no_antesedentes = fields.Binary(
        string='Carta Antecedentes',
    )
    acta_nacimiento = fields.Binary(
        string='Acta de Nacimiento',
    )
    recomendacion1 = fields.Binary(
        string='Carta de recomendación',
    )
    recomendacion2 = fields.Binary(
        string='Carta de recomendación',
    )
    emp_contrato = fields.Binary(
        string='Contrato',
    )