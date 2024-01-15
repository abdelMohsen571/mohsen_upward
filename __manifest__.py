# -*- coding: utf-8 -*-
{
    'name': "Upward Project",

    'summary': """
        School Project is bla bla bla
        """,

    'description': """
        Long des    """,

    'author': "Upward Company",
    'website': "https://upward.sa",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/students_view.xml',
        'views/teachers_view.xml',
        'views/course_view.xml',
        'views/menu_items_view.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': True,
    # only loaded in demonstration mode
    'demo': [],
}
