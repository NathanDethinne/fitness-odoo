{
    "name": "Fitness App",
    "version": "1.0",
    "depends": ["base"],
    "installable": True,
    "application": True,
    'depends': ['web'],  # Critical for odoo.define availability
    'data': [
        'security/ir.model.access.csv',
        'views/workout_views.xml',
        'views/exercise_views.xml',
        'views/catalog_views.xml',
        'views/set_views.xml',
        'data/progress_views.xml',
        'views/menus.xml',
        'data/exercise_catalog_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'fitness_app/static/src/js/progress_chart.js',
            'fitness_app/static/src/xml/my_progress.xml',
        ],
    }
}