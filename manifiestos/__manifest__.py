{
    'name': 'Manifiestos',
    'version': '1.0',
    'summary': 'Aplicación para registrar manifiestos de residuos.',
    'author': 'Fernando Rodriguez',
    'depends': ['base','product','hr'],  # Dependencias de otros módulos
    'data': [
        'views/manifiesto_view.xml',
        'views/templates.xml',
        'reports/aguascalientes.xml',
        'reports/jaliscosalto.xml',
        'reports/guanajuato.xml',
        'reports/nayarit.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}
