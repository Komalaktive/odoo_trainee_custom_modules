
{
    'name': "practical",

    'summary': """
       Practical Task""",

    'description': """ Long description of module's purpose """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '14.0.1.0.0',
    'depends': ["base", "hr", "hr_recruitment"],
    'data': [
        'security/ir.model.access.csv',
        'views/task_views.xml',
    ],
  
    'demo': [
        # 'demo/demo.xml',
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}
