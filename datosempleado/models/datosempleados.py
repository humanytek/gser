from odoo import fields, models

class datosEmpleados (models.Model):
    _inherit="hr.employee"
    domicilio = fields.Char(
        string="Domicilio",
    )
    estudios = fields.Char(
        string="estudios",
    )
    imss = fields.Char(
        string="imss",
    )
    infonavit = fields.Char(
        string="infonavit",
    )
    curp = fields.Char(
        string='curp',
    )
    rfc = fields.Char(
        string='ine',
    )
    ine = fields.Char(
        string='ine',
    )
    no_antesedentes = fields.Char(
        string='no_antesedentes',
    )
    acta_nacimiento = fields.Char(
        string='acta_nacimiento',
    )
    recomendacion1 = fields.Char(
        string='recomendacion1',
    )
    recomendacion2 = fields.Char(
        string='recomendacion2',
    )
    emp_contrato = fields.Char(
        string='emp_contrato',
    )