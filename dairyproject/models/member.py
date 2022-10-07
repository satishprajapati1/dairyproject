from datetime import date
from odoo import fields,models,api

class Member(models.Model):
    _name = 'member'
    _description = 'Dairy Member'
    _order = 'member_id'

    member_id = fields.Integer(string='Member no.')
    name = fields.Char(string='Member name')
    # partner_id = fields.Many2one('res.partner',required=True,string = 'Member name')
    dob = fields.Date(string="Date of Birth",required=True)
    gender = fields.Selection([('m','Male'),('f','Female'),('o','Other')],required=True)
    age = fields.Integer(compute='_compute_age',readonly=True)
    address = fields.Text()
    mobile = fields.Char(required=True)
    joining_date = fields.Date()    

    @api.onchange("dob")
    def _compute_age(self):
        for record in self:
            today = date.today()
            record.age = today.year - record.dob.year -((today.month, today.day) < (record.dob.month , record.dob.day))