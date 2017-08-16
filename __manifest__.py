# -*- coding: utf-8 -*-
{
    'name': "thanos_secundary_menu",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['website', 'website_blog', 'sale'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/layout.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}