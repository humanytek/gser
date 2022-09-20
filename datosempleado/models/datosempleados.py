from odoo import fields, models

class datosEmpleados (models.Model):
    _inherit="hr.employee"
    #Documentacion personal
    acta_nacimiento = fields.Binary(
        string='Acta de Nacimiento',
    )
    domicilio = fields.Binary(
        string="Comp. Domicilio",
    )
    estudios = fields.Binary(
        string="Comp. Estudios",
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
    
    
    #Seguro
    imss = fields.Char(
        string="Numero IMSS",
    )
    alta_patronal = fields.Date(
        string="Fecha de alta patronal",
    )
    alta_imss = fields.Binary(
        string="Alta IMSS",
    )
    infonavit = fields.Binary(
        string="Comp. Infonavit",
    )
    
    #Contratos
    emp_fechaIngreso = fields.Date(
        string='Fecha de ingreso',
    )
    emp_contrato = fields.Binary(
        string='Contrato',
    )
    emp_reglamento = fields.Binary(
        string='Reglamento',
    )
    emp_codigoetica = fields.Binary(
        string='Codigo Etica',
    )
    emp_bajafecha = fields.Date(    
        string='Fecha Baja',
    )
    emp_baja = fields.Binary(
        string='Baja',
    )
    emp_motivo_baja = fields.Text(
        string='Motivo',
    )  
    no_antesedentes = fields.Binary(
        string='Carta Antecedentes',
    )   
    recomendacion1 = fields.Binary(
        string='Carta de recomendación',
    )
    recomendacion2 = fields.Binary(
        string='Carta de recomendación',
    )
    
    #Vehiculo
    licencia = fields.Binary(
        string='Licencia',
    )
    vigencia = fields.Date(
        string='Vigencia',
    )
    chofer_examen = fields.Binary(
        string='Examen de manejo',
    )
    vigencia_exam = fields.Date(
        string='Vigencia',
    )
    #responsivas
    res_unidad = fields.Binary(
        string='Unidad',
    )
    res_llavecaseta = fields.Binary(
        string='Llave caseta',
    )
    res_llavedisel = fields.Binary(
        string='Llave Disel',
    )
    res_telefono = fields.Binary(
        string='Telefono',
    )
    res_equipo = fields.Binary(
        string='Equipo',
    )
    res_resguardo1 = fields.Binary(
        string='Resguardo 1',
    )
    res_resguardo2 = fields.Binary(
        string='Resguardo 2',
    )