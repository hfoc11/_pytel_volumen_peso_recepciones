# -*- coding: utf-8 -*-
{
    'name': "Mostrar Peso y Volumen en la recepcion",

    'summary': """
                Mostrar Peso y Volumen en la recepcion
    """,

    'description': """
    
    """,
    'author': "Pytel",
    'version': '0.1',

    'depends': [
        'base',
        'product',
        'stock',
        'delivery',
    ],

    'data': [
        'views/stock_move.xml',
    ],
    'installable': True,
   
}