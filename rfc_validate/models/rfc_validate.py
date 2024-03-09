from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class RfcValidate (models.Model):
    _inherit="res.partner"
    
    def write(self, vals):
        res = super(RfcValidate, self).write(vals)
        vat_validate = self.env['res.partner'].search([('vat', '=', self.vat,), ('vat', '!=', False,)])
        if len(vat_validate) > 1:
            raise ValidationError(_('Ya existe un contacto con el RFC registrado, por favor verificar.'))
        return res
    
    def create(self, vals):
        res = super(RfcValidate, self).create(vals)
        vat_validate = self.env['res.partner'].search([('vat', '=', self.vat,), ('vat', '!=', False,)])
        if len(vat_validate) > 1:
            raise ValidationError(_('Solo puede existir un contacto con el RFC registrado, por favor verificar.'))
        return res