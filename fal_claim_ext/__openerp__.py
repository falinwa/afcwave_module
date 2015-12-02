# -*- coding: utf-8 -*-
{
    "name": "STC-08_Claim Ext",
    "version": "1.0",
    'author': 'Falinwa Hans',
    "description": """
    Module to add additional feature for claim.
    """,
    "depends" : ['stock', 'sale_stock', 'claim_from_delivery','crm','delivery'],
    'init_xml': [],
    'update_xml': [

        'security/security.xml',
        'security/ir.model.access.csv', 
        'wizard/claim_delivery_wizard.xml',
        'views/claim_ext_views.xml',
        'sequence.xml',
    ],
    'css': [],
    'js' : [],
    'installable': True,
    'active': False,
    'application' : False,
    'sequence': 150,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: