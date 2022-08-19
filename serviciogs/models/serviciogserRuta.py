from odoo import fields, models, api

class ServicioRuta(models.Model):
    _name = 'serviciogserRuta'
    _description = 'Rutas'

    contacto_facturacion = fields.Char(
        string="Conctacto Facturacion",
        
    )
    email_facturacion = fields.Char(
        string="email",
     
    )
    ord_vent = fields.Char(
        string ="Orden de venta",
    )
   
