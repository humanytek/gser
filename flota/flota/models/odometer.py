from odoo import fields, models, api

class OdometerSerrano(models.Model):
    _inherit = "project.task"
    
    def action_fsm_validate(self):
        res = super().action_fsm_validate()
        if self.estatus_viaje == "9":
            # vehicle = ['fleet.vehicle'].browse(self.vehiculo)
            date_end = self.planned_date_end.date()
            date_start = self.planned_date_begin.date()
            #address_id.parent_id
            # driver_id = self.env['res.partner'].browse(self.conductor.address_home_id.id)
            history_driver = self.env['fleet.vehicle.assignation.log'].create({'vehicle_id': self.vehiculo.id,
                                                        'driver_id': self.conductor.address_home_id.id,
                                                        'date_end': date_end,
                                                        'date_start' : date_start,
                                                        })
            
            odometer = self.env['fleet.vehicle.odometer'].create({'vehicle_id': self.vehiculo.id,
                                                        'date': date_end,
                                                        'driver_id': self.conductor.address_home_id.id,
                                                        'value': self.km_viaje, 
                                                        })
            return history_driver,odometer
        return res