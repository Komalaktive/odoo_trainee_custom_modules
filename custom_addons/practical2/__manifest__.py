
{
    'name': "practical2",

    'summary': """
        Practical Task""",

    'description': """
        Task
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base'],

   
    'data': [
        'security/ir.model.access.csv',
        'views/track_order_views.xml',
        # 'views/templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
