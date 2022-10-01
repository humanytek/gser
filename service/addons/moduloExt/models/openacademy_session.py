# -*- coding: utf-8 -*-
from datetime import timedelta


from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class OpenacademySession(models.Model):
    _name = 'openacademy.session'
    _description = 'OpenAcademy Session'

    name = fields.Char(
        required=True,
    )
    start_date = fields.Date(
        default=fields.Date.today,
    )
    duration = fields.Float(
        digits=(6, 2),
        help=_("Duration in days"),
    )
    seats = fields.Integer(
        string="Number of seats",
    )
    instructor_id = fields.Many2one(
        comodel_name='res.partner',
        domain=[
            '|',
            ('instructor', '=', True),
            ('category_id.name', 'ilike', "Teacher"),
        ],
    )
    course_id = fields.Many2one(
        comodel_name='openacademy.course',
        ondelete='cascade',
        required=True,
    )
    attendee_ids = fields.Many2many(
        comodel_name='res.partner',
    )
    taken_seats = fields.Float(
        compute='_taken_seats',
    )
    active = fields.Boolean(
        default=True,
    )
    end_date = fields.Date(
        store=True,
        compute='_get_end_date',
        inverse='_set_end_date',
    )
    attendees_count = fields.Integer(
        compute='_get_attendees_count',
        store=True,
    )
    color = fields.Integer()

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for record in self:
            if not record.seats:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * len(record.attendee_ids) / record.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': _("The number of available seats may not be negative"),
                },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': "Too many attendees",
                    'message': "Increase seats or remove excess attendees",
                },
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for record in self:
            if record.instructor_id and record.instructor_id in record.attendee_ids:
                raise ValidationError("A session's instructor can't be an attendee")

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            duration = timedelta(days=record.duration, seconds=-1)
            record.end_date = record.start_date + duration

    def _set_end_date(self):
        for record in self:
            if not (record.start_date and record.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            record.duration = (record.end_date - record.start_date).days + 1

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for record in self:
            record.attendees_count = len(record.attendee_ids)
