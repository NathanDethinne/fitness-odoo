from odoo import models, fields, api

class Exercise(models.Model):
    _name = "fitness.exercise"
    _description = "Exercise"

    name = fields.Char(string="Exercise Name", required=True)
    muscle_group = fields.Char(string="Muscle Group")

    workout_id = fields.Many2one(
        comodel_name="fitness.workout",
        string="Workout"
    )

    set_ids = fields.One2many(
        comodel_name="fitness.set",
        inverse_name="exercise_id",
        string="Sets"
    )

    exercise_volume = fields.Float(compute='_compute_exercise_volume', store=True)
    @api.depends('set_ids.reps', 'set_ids.weight')
    def _compute_exercise_volume(self):
        for record in self:
            total = 0    
        for s in record.set_ids:
            total += (s.reps or 0) * (s.weight or 0)
        record.exercise_volume = total

    