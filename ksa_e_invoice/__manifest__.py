{
    "name": "KSA E-Invoice",
    "version": "13.0.0.0.1",
    "category": "Point Of Sale",
    "version": "14.0.0.0.1",
    'live_test_url': 'https://youtu.be/nqlsBJ4ZkL8',
    'summary': "odoo POS Electronic Invoice",
    'description': """
    odoo POS Electronic Invoice .
    """,
    "author": "Alhaditech",
    "website": "www.alhaditech.com",
        'license': 'AGPL-3',
    'images': ['static/description/background.jpeg','static/description/background2.png'],
    "depends": [
        'base','sale','doctor','point_of_sale'
    ],
    'price': 50, 'currency': 'EUR',
    'images': ['static/description/background.png'],
    "depends": [
        'base', 'point_of_sale'
    ],
    "data": [
        'views/assets.xml',
        ],
    'qweb': ['static/src/xml/pos.xml'],
    "installable": True,
    'application': True,
}
