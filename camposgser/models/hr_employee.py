from odoo import fields, models

class campos_ajuste (models.Model):
    _inherit = "hr.employee"

    curp_mx = fields.Char(
        string="CURP UPGRADE",
        groups="hr.group_hr_user",
    )

    identification_id = fields.Char(
        string="INE UPGRADE1",
        groups="hr.group_hr_user",
    )

    f_ine = fields.Char(
        string="INE UPGRADE2",
        groups="hr.group_hr_user",
    )

    f_rfc = fields.Char(
        string="RFC UPGRADE",
        groups="hr.group_hr_user",
    )

    OPCIONES_CAMPO_SELECCION = [
        ("0", "Selecciona"),
        ("1", "Un hijo"),
        ("2", "2 Hijos"),
        ("3", "3 Hijos"),
        ("4", "4 Hijos"),
        ("5", "5 Hijos"),
        ("6", "6 Hijos"),
        ("7", "7 Hijos"),
        ("8", "8 Hijos"),
    ]

    campo_de_seleccion = fields.Selection(
        selection=OPCIONES_CAMPO_SELECCION,
        string="Cantidad de Hijos",
        groups="hr.group_hr_user",
    )
    
    hijo_1 = fields.Char(
        string="Hijo 1",
        invisible=True,
        groups="hr.group_hr_user",
    )
    hijo_2 = fields.Char(
        string="Hijo 2",
        invisible=True,
        groups="hr.group_hr_user",
    )
    hijo_3 = fields.Char(
        string="Hijo 3",
        invisible=True,
        groups="hr.group_hr_user",
    )
    hijo_4 = fields.Char(
        string="Hijo 4",
        invisible=True,
        groups="hr.group_hr_user",
    )
    hijo_5 = fields.Char(
        string="Hijo 5",
        invisible=True,
        groups="hr.group_hr_user",
    )
    hijo_6 = fields.Char(
        string="Hijo 6",
        invisible=True,
        groups="hr.group_hr_user",
    )
    hijo_7 = fields.Char(
        string="Hijo 7",
        invisible=True,
        groups="hr.group_hr_user",
    )
    hijo_8 = fields.Char(
        string="Hijo 8",
        invisible=True,
        groups="hr.group_hr_user",
    )

    edad_hijo_1 = fields.Integer(
        string="Edad hijo 1",
        invisible=True,
        groups="hr.group_hr_user",
    )
    edad_hijo_2 = fields.Integer(
        string="Edad hijo 2",
        invisible=True,
        groups="hr.group_hr_user",
    )
    edad_hijo_3 = fields.Integer(
        string="Edad hijo 3",
        invisible=True,
        groups="hr.group_hr_user",
    )
    edad_hijo_4 = fields.Integer(
        string="Edad hijo 4",
        invisible=True,
        groups="hr.group_hr_user",
    )
    edad_hijo_5 = fields.Integer(
        string="Edad hijo 5",
        invisible=True,
        groups="hr.group_hr_user",
    )
    edad_hijo_6 = fields.Integer(
        string="Edad hijo 6",
        invisible=True,
        groups="hr.group_hr_user",
    )
    edad_hijo_7 = fields.Integer(
        string="Edad hijo 7",
        invisible=True,
        groups="hr.group_hr_user",
    )
    edad_hijo_8 = fields.Integer(
        string="Edad hijo 8",
        invisible=True,
        groups="hr.group_hr_user",
    )

    beneficiario_1 = fields.Char(
        string="Beneficiario 1",
        invisible=True,
        groups="hr.group_hr_user",
    )
    beneficiario_2 = fields.Char(
        string="Beneficiario 2",
        invisible=True,
        groups="hr.group_hr_user",
    )
    
    beneficiario_porce_1 = fields.Integer(
        string="Procentaje 1",
        invisible=True,
        groups="hr.group_hr_user",
    )
    beneficiario_porce_2 = fields.Integer(
        string="Procentaje 2",
        invisible=True,
        groups="hr.group_hr_user",
    )

    beneficiario_par_1 = fields.Char(
        string="Parentesco 1",
        invisible=True,
        groups="hr.group_hr_user",
    )
    beneficiario_par_2 = fields.Char(
        string="Parentesco 2",
        invisible=True,
        groups="hr.group_hr_user",
    )
