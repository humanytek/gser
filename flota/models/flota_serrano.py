from odoo import fields, models,api

class FlotaSerrano(models.Model):
#    _name = 'flota.serrano'
#    _description = 'Flota Serrano'
    _inherit = "sale.order"
    marca = fields.Char(
        string="Marca",
    )
    modelo = fields.Char(
        string="Modelo",
    )
    km = fields.Float(
        string="Kilometraje"
    )
    rendimiento = fields.Float(
        default=2.2,
        string="Rendimiento"
    )
    disel = fields.Float(
        compute='_compute_disel',
    )

    @api.depends("km", "rendimiento")
    def _compute_disel(self):
        for record in self:
            record.disel = record.km / record.rendimiento
    
    conductor = fields.Many2one(
        comodel_name='hr.employee',
        ondelete='set null',
        index=True,
    )
#    _sql_constraints = [
#        ('name_description_check',
#         'CHECK(name != description)',
#         "The title of the course should not be the description"),

#        ('name_unique',
#         'UNIQUE(name)',
#         "The course title must be unique"),
#    ]
    
#    no_economico = fields.Char(
#        string="No.Económico",
#        required=True,
#    )
#    placa = fields.Char(
#        string="Placas",
#        required=True,
#    )
    

    
    #def fun_rend(self):
     #   return '2.2'

   
    #def _onchange_disel(self):
    # set auto-changing field
    #    self.disel = self.km / self.rendimiento
        # Can optionally return a warning and domains
    #    return {
    #        'warning': {
    #            'title': "Something bad happened",
    #            'message': "It was very bad indeed",
    #        }
    #    }
#    no_chasis = fields.Char(
#        string="Chasis",
#        required=True,
#    )
#    f_registro = fields.Char(
#        string="Fecha de Registro",
#        required=True,
#    )
#    empresa = fields.Char(
#        string="Empresa",
#        required=True,
#    )
  
#    def copy(self, default=None):
#        default = dict(default or {})
#        copied_count = self.search_count(
#            [('name', '=like', u"Copy of {}%".format(self.name))])
#        if not copied_count:
#            new_name = u"Copy of {}".format(self.name)
#        else:
#            new_name = u"Copy of {} ({})".format(self.name, copied_count)
#
#        default['name'] = new_name
#        return super(FlotaSerrano, self).copy(default)
