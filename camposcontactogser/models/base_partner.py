from odoo import fields, models

class campos_ajuste_contacto (models.Model):
    _inherit = "base.partner"

    f_licencia = fields.Date(
        string="vigencia de licencia",
    )

    doc_f_licencia = fields.Binary(
        string="Licencia",
        groups="hr.group_hr_user",
    )