from odoo import fields,models,api

class CattleBreed(models.Model):
    _name = 'cattle.breed'
    _description = 'Cattle Breed'
    _order = 'name'

    name = fields.Char(required=True,string='Breed name')
    sequence = fields.Integer('Sequence', default=1, help="Used to order stages. Lower is better.")

    _sql_constraints = [
        ('breed_uniq','unique(name)','Cattle Breed must be unique')
    ]

class Cattle(models.Model):
    _name = 'cattle'
    _description = 'Cattle'
    _order = 'cattle_id'

    cattle_id = fields.Integer(required=True)
    name = fields.Char()
    cattle_type = fields.Selection([('cow','Cow'),('buffalo','Buffalo'),('goat','Goat')],required=True)
    cattle_breed = fields.Many2one('cattle.breed',required=True)
    height = fields.Float()
    weight = fields.Float()
    body_condition = fields.Selection([('fit','Fit'),('sick','Sick'),('weak','Weak')])
    owner_name = fields.Many2one('member',required=True)

    _sql_constraints = [
        ('id_uniq','unique(cattle_id)','Cattle Id must be unique')
    ]