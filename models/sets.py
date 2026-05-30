from odoo import models, fields, api

class Set(models.Model):
    _name = "fitness.set"
    _description = "Set"
    
    reps = fields.Integer(string="Repetitions")
    weight = fields.Float()

    exercise_id = fields.Many2one(
        comodel_name="fitness.exercise",
        string="Exercise",
        ondelete='cascade'
        #consistency
    )
    
    @api.onchange('exercise_id')
    #for interactivity
    def _onchange_exercise_id(self):
    #convention
        exercise_records = self.env['fitness.exercise'].search([
            ('exercise_date', '<', self.exercise_id._origin.exercise_date),
    #_origin to access the db
            ('catalog_id', '=', self.exercise_id._origin.catalog_id.id)],
            order='exercise_date desc',
            limit=1)
        #searches for the last exercise performances, not the current ones
        if not exercise_records:
            return
        first_set = self.env['fitness.set'].search([('exercise_id', '=', exercise_records.id)], order='id asc', limit=1)
        #searches for the first set
        if first_set.exists():
            if first_set.reps >= 8:
                if first_set.exercise_id.catalog_id.equipment in ("Barbell", "Smith Machine", "Plate Loaded Machine"):
                    #handles loaded independently for plate loaded machines could have an increment of 1.25
                    self.weight = first_set.weight + 2.5
                elif first_set.exercise_id.catalog_id.equipment in ("Cable", "Machine"):
                    self.weight = first_set.weight + 2
                elif first_set.exercise_id.catalog_id.equipment == "Dumbbell":
                    if first_set.weight < 10:
                        self.weight = first_set.weight + 1
                    elif first_set.weight >= 10:
                        self.weight = first_set.weight + 2
            else:
                self.weight = first_set.weight
        
    set_date = fields.Date(
        string='Set Date',
        related='exercise_id.workout_id.date',
        readonly=True
    )
    #simplifies OWL query