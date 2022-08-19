from odoo import fields, models

class servicioGSerRuta (models.Model):
    contacto_facturacion = fields.Char(
        string="Contacto Facturación",
    )
    
    email_facturacion = fields.Char(
        #related ='partner_id.email',
        string="E-mail Facturación",
    )
  
    ord_vent = fields.Char(
        string="Orden de Venta",
        #comodel_name='sale.order',
        #ondelete='set null',
        #index=True,
    )

