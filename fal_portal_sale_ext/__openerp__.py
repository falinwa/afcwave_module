# -*- coding: utf-8 -*-
{
    "name": "SAL-09_Portal Sale",
    "version": "1.0",
    'author': 'Falinwa Hans',
    "description": """
    Module to give feature to portal sale to create an order.
    """,
    "depends" : ['base', 'sale', 'sale_stock', 'portal_sale', 'web_tree_image', 'fal_sales_report_product_image'],
    'init_xml': [],
    'data': [
    ],
    'update_xml': [
        'security/ir.model.access.csv',
        'sale_view.xml',
    ],
    'css': [],
    'js' : [
    ],
    'qweb': [],
    'installable': True,
    'active': False,
    'application' : False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: