from odoo import fields, models, api

class ServicioRuta(models.Model):
    
    contacto_facturacion = fields.Char(
        string="Conctacto Facturacion",
        
    )
    email_facturacion = fields.Char(
        string="email",
     
    )
    ord_vent = fields.Char(
        string ="Orden de venta",
    )
   
