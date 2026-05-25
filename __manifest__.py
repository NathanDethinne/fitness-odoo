{
    "name": "Fitness App",
    "version": "1.0",
    "depends": ["base"],
    "installable": True,
    "application": True,
    'data': [
        'security/ir.model.access.csv',
        'views/workout_views.xml',
        'views/exercise_views.xml',
        'views/catalog_views.xml',
        'views/set_views.xml',
        'views/menus.xml',
        'data/exercise_catalog_data.xml',
    ],
}