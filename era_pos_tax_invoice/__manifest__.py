# -*- coding: utf-8 -*-
{
    'name': "Electronic invoice KSA - POS | qrcode | ZATCA | vat | e-invoice | tax | Zakat",
    "version" : "13.0.0.3",
    "category" : "Accounting",
    'description': """
        Electronic invoice KSA - POS
    """,
    'author': "logman",
    'email': "logmano@gmail.com",
    'website': "https://logman.com",
    'category': 'accounting',
    'price': 100,  
    'currency': 'USD',
    'version': '0.1',
    'license': 'AGPL-3',
    'images': ['static/description/main_screenshot.png'],
    'depends': ['base', 'account', 'point_of_sale',],
    'data': [
        'views/pos_config.xml',
    ],
    'qweb': ['static/src/xml/pos.xml'],

}
