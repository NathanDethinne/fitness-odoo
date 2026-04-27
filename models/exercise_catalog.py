from odoo import models, fields

class Catalog(models.Model):
    _name = "fitness.catalog"
    _description = "Catalog"

    name = fields.Char(string="Exercise Name", required=True)
    muscle_group = fields.Char(string="Muscle Group")
    equipment = fields.Char(string="Equipment")
    description = fields.Text()