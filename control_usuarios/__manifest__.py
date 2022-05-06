# -*- coding: utf-8 -*-
{
    'name': "Control Usuarios",

    'summary': """
        Control de cada cliente en el gimnasio """,

    'description': """
        Módulo para controlar clientes
    """,

    'author': "Tony Center",
    'website': "https://www.tugimnasio.es/listings/tony-center/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administration',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'hr'],

    # always loaded
    'data': [
        'security/control_usuarios_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/control_usuarios.clientes_report.xml',
        'data/control_usuarios_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],


# Indicamos que es una aplicación

'application': True,

}
