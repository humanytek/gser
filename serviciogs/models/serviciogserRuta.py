from odoo import fields, models

class ServicioRuta(models.Model):
    _name = 'servicio.ruta'
    _description = 'Rutas'

    contacto_facturacion = fields.Char(
        string="Conctacto Facturacion",
        required=True,
    )
    email_facturacion = fields.Char(
        string="email",
        required=True,
    )
    ord_vent = fields.Char(
        string ="Orden de venta",
    )
   
