# -*- coding: utf-8 -*-
{
    'name': "Anglo Saxon",

    'summary': """
        Company - Adds Active toggle button and checkbox to enable anglo-saxon accounting
    """,

    'description': """
        Adds "Active/Archived" toggle button and a checkbox to enable/dissable anglo-saxon accounting under "Settings --> Companies" view
    """,

    'author': "davidc5153@gmail.com",
    'website': "",

    # Categories ...
    # https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    'category': 'Accounting',
    'version': '1',

    # Dependancies
    'depends': [
        'base',
        'account_invoicing'
    ],

    # Loaded resources
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_company_anglo_saxon_view.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': False,
}
