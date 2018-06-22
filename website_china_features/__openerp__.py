# -*- coding: utf-8 -*-
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    'name': "Website China Features",
    'summary': 'Build Your China Features Website',
    'author': "renjie <i@renjie.me>",
    'website': "https://renjie.me",
    'support': 'i@renjie.me',
    'category': 'Website',
    'version': '0.2',
    'depends': ['website'],
    'data': [
        'views/website_templates.xml',
        'views/res_config.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'images': [
        'static/description/main_screenshot.png',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}