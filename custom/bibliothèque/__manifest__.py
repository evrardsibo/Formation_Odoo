# -*- coding: utf-8 -*-
{
    'name': "bibliothèque",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

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
        'views/views.xml',
        'views/templates.xml',
        'views/books_views.xml',
        'views/member_views.xml',
        'views/genre_tag_views.xml',
        'views/author_views.xml',
        'views/library_loan_views.xml',
        'wizard/wizard_book.xml',
        'wizard/wizard_book1.xml',
         'data/book_data.xml',
        'data/gender_data.xml',
         'data/author_data.xml',
        'data/member_data.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

