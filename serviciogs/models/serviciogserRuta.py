from odoo import fields, models

class servicioruta(models.Model):
    _name = 'servicio.ruta'
    _description = 'Rutas'

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
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
   
    def copy(self, default=None):
        default = dict(default or {})
        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(servicioGSer, self).copy(default)
