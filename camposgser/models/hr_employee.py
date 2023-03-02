from odoo import fields, models

class campos_ajuste (models.Model):
    _inherit = "hr.employee"

    work_phone = fields.char(
    string="Telefonoo",
    )