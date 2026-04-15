from odoo import models, fields

class Set(models.Model):
    _name = "fitness.set"
    _description = "Set"
    
    reps = fields.Integer(string="Repetitions")
    weight = fields.Float()

    exercise_id = fields.Many2one(
        comodel_name="fitness.exercise",
        string="Exercise"
        )