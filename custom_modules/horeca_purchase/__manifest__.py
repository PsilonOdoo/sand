# -*- coding: utf-8 -*-
{
    'name': "horeca_purchase",

    'summary': """
        Horeca Inherited Purchase Module""",

    'description': """
        Long Description about module
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase',
                'purchase_requisition',
                'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/inherit_purchase_order.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
