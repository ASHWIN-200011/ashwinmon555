 
{
    'name': 'POS restaurant depend',
    'category': 'Services',
    'version': '16.0.1.1.0',
    'author': 'Terabits Technolab ',
    'website': 'https://www.terabits.xyz/apps/16.0/pos_restaurant_depends_bits',
    'summary': 'This module contains pos restaurant-related customizations depending on delight_pos_theme_bits',
    'description': """ This module contains pos restaurant-related customizations depending on delight_pos_theme_bits """,
    'depends': [
        'pos_restaurant',   
    ],
    'assets': {
        'point_of_sale.assets': [  
            '/pos_restaurant_depends_bits/static/src/xml/FloorScreen.xml',
            '/pos_restaurant_depends_bits/static/src/js/FloorScreen.js',
            '/pos_restaurant_depends_bits/static/src/js/TableWidget.js',
            '/pos_restaurant_depends_bits/static/src/js/FloorScreenMenu.js',
            '/pos_restaurant_depends_bits/static/src/xml/FloorScreenMenu.xml', 
        ],
    },
    'images': [
        'static/description/banner.png'
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OPL-1', 
}
