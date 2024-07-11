{
    'name': 'clg Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage school students',
    'description': """
    This module helps you to manage school students.
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/school.xml',
    ],
    'installable': True,
    'application': True,
}
