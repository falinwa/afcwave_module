# -*- coding: utf-8 -*-
{
    "name": "AFC WAVE Extends Module",
    "version": "1.0",
    'author': 'Falinwa Hans',
    "description": """
    Module to add additional field for AFC WAVE
    """,
    "depends" : [
        'base', 'report', 'stock', 'sale', 'portal_sale', 'fal_portal_sale_ext', 'purchase', 'website_sale'
        ],
    'init_xml': [],
    'update_xml': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'sale_view.xml',
        'purchase_view.xml',
        'country_manager_view.xml',
    ],
    'css': [],
    'js' : [],
    'installable': True,
    'active': False,
    'application' : False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: