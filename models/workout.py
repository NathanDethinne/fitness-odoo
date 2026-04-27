from odoo import models, fields, api

class Workout(models.Model):
    _name = "fitness.workout"
    _description = "Workout"

    name = fields.Char(required=True)
    date = fields.Date(required=True)

    exercise_ids = fields.One2many(
        comodel_name="fitness.exercise",
        inverse_name="workout_id",
        string="Exercises"
    )

    #workout_volume = fields.Float(compute='_compute_workout_volume', store=True)
    #@api.depends('exercise_ids.exercise_volume')
    #def _compute_workout_volume(self):
        #for record in self:
            #total = 0    
            #for s in record.exercise_ids:
                #total += (s.exercise_volume or 0)
            #record.workout_volume = total

    #strongest_exercise_id = fields.Many2one(
        #comodel_name="fitness.exercise",
        #string="Strongest exercise"
    #)
#