from odoo import models, fields, api

class Exercise(models.Model):
    _name = "fitness.exercise"
    _description = "Exercise"

    workout_id = fields.Many2one(
        comodel_name="fitness.workout",
        string="Workout"
    )

    exercise_id = fields.Many2one(
        comodel_name="fitness.catalog",
        string="Catalog"
    )

    set_ids = fields.One2many(
        comodel_name="fitness.set",
        inverse_name="exercise_id",
        string="Sets"
    )

     #exercise_volume = fields.Float(compute='_compute_exercise_volume', store=True)
    #@api.depends('set_ids.reps', 'set_ids.weight')
    #def _compute_exercise_volume(self):
        #for record in self:
            #total = 0    
        #for s in record.set_ids:
            #total += (s.reps or 0) * (s.weight or 0)
        #record.exercise_volume = total