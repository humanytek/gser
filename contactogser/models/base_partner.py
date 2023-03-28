from odoo import fields, models

class campos_ajuste_contacto (models.Model):
    _inherit = "res.partner"

    f_licencia = fields.Date(
        string="Vigencia de licencia",
    )