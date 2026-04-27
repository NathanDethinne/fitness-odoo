{
    "name": "Fitness App",
    "version": "1.0",
    "depends": ["base"],
    "installable": True,
    "application": True,
    'data': [
        'security/ir.model.access.csv',
        'views/workout_views.xml',
        'data/exercise_catalog_data.xml'
    ],
}