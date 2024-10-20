{
    'name' : 'Register Payment States',
    # 'version': '17.0.1.0.1',
    'summary': 'Account Payment states',
    # 'sequence': 1,
    'category': 'Accounting & Finance',
    'website': 'https://erisp.net',
    'author': 'ERISP (Pvt.) Ltd.',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'description': """ Register Payment States
                   """,
    'depends' : [
                    'account'
                ],
    'data': [
                'security/security.xml',
                'views/account_move.xml',
                'views/account_payment.xml',
            ],
}
