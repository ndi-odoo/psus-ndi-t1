# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary':"""Academy app""",
    
    'description': """
       my description""",
    
    'author': 'ndi',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    
    'version' : '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views'
    ],
    'demo': [
        'demo/academy_demo.xml'
    ],
    'license': 'OEEL-1',
    
}