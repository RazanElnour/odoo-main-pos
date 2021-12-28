# -*- coding: utf-8 -*-
{
    'name': "POS Direct Login",

    'summary': """
        Helps to directly login to POS.""",

    'description': """
        Log in to configured POS shop to save time.""",

    'author': "Nabil YAHIA",
    'license': 'AGPL-3',
    'category': 'Point of Sale',
    'version': '13',
    'installable': True,
    'auto_install': False,
    'depends': ['point_of_sale'],
    'data': [
        'views/res_users.xml',
    ],
}
