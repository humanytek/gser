# -*- coding: utf-8 -*-
import json
import base64

from odoo import http
from odoo.http import Controller, request, route
import logging
import webbrowser


_logger = logging.getLogger(__name__)

try:
    from OpenSSL import crypto
except ImportError:
    _logger.warning('OpenSSL library not found. If you plan to use l10n_ar_edi, please install the library from https://pypi.python.org/pypi/pyOpenSSL')

class controllersUbicaloApi(http.Controller):
    
    def buscar_en_mapa(self, latitud, longitud):
        url = f"https://www.google.com/maps/search/?api=1&query={latitud},{longitud}"
        webbrowser.open(url)

    @http.route('/endpoint/ubicalo', type='http', auth='public', method='POST', website=True, csrf=False)
    def ubicalo_response (self, **post):
        data = {"Placas": 'GTM-0345',
                "IMEI": '8637190633297558',
                "Codigo": 'Por Tiempo',
                "Latitud": 21.0832583,
                "Longitud": -101.624985,
                "Altitud": 1815,
                "Velocidad": 50,
                "Odometro": 16884,
                "Rumbo": 128,
                "Direccion": 'Zetta, Industrial Delta, 37545',
                "Estado": 'Zacatecas',
                "Localidad": 'Zacatecas',
                "Pais": 'México',
                "CodigoEvento": 'Por Tiempo',
        }
        data_maps_lat = str(data.get('Latitud'))
        data_maps_long = str(data.get('Longitud'))
        return self.buscar_en_mapa(data_maps_lat, data_maps_long)
    