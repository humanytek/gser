{
    'name': 'Servicio Rutas',
    'version': '13.0.0.4.0',
    'author': 'GSerrano Lagos de Moreno',
    'website': '',
    'license': 'LGPL-3',
    'depends': [
        "industry_fsm",
        "project",
        "sale_management",
        "fleet"
    ],
    'data': [
        # security
        # data
        # demo
        # reports
        'report/reports.xml',
        'report/ticket_viaje.xml',
        'report/ticket_cliente.xml',
        #'report/proceso_lavado.xml',
        # # views
        'views/serviciogser.xml',
        'views/serviciogserprimario.xml',
    ],
}
