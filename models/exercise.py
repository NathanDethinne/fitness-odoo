from odoo import models, fields, api

class Exercise(models.Model):
    _name = "fitness.exercise"
    _description = "Exercise"

    workout_id = fields.Many2one(
        comodel_name="fitness.workout",
        string="Workout",
        required=True,
        ondelete='cascade'
        #ability to delete all exercises when workout deleted instead of error
    )

    catalog_id = fields.Many2one(
        comodel_name="fitness.catalog",
        string="Catalog"
    )

    set_ids = fields.One2many(
        comodel_name="fitness.set",
        inverse_name="exercise_id",
        string="Sets"
    )

    exercise_date = fields.Date(
        related='workout_id.date',
        store=True
    )
    #more efficient to let db order

    exercise_volume = fields.Float(compute='_compute_exercise_volume', store=True)
    @api.depends('set_ids.reps', 'set_ids.weight')
    def _compute_exercise_volume(self):
        for record in self:
            total = 0    
            for set_record in record.set_ids:
                total += (set_record.reps or 0) * (set_record.weight or 0)
            record.exercise_volume = total