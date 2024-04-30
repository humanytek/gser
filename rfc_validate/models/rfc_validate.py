from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class RfcValidate (models.Model):
    _inherit="res.partner"
        
    @api.onchange('vat', 'company_id')
    def rfcvalidate(self):
        # res = super(RfcValidate, self)._compute_same_vat_partner_id(vals)
        vat_validate = self.env['res.partner'].search([('vat', '=', self.vat,), ('vat', '!=', False,)])
        if len(vat_validate) > 0 :
            self.vat = False
            raise ValidationError(_('Ya existe un contacto con el RFC registrado, por favor verificar.'))
        # return res
    
    def create(self, vals):
        res = super(RfcValidate, self).create(vals)
        
        vat_validate = self.env['res.partner'].search([('vat', '=', self.vat,), ('vat', '!=', False,)])
        if len(vat_validate) > 0:
            raise ValidationError(_('Solo puede existir un contacto con el RFC registrado, por favor verificar.'))
        
        # 'copia' in vals.get('name')
        return res