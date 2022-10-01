# -*- coding: utf-8 -*-
from odoo import fields, models


class ServiceExt(models.Model):
    _name = 'service.ext'
    _description = 'Service Extern'

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
  
    name = fields.Char(
        string="Title",
        required=True,
    )
    
    description = fields.Text(
    )
    x_carga =fields.Char(
        string="Carga",                                                                                                                                                                   
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
        return super(ServiceExt, self).copy(default)
