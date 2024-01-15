from datetime import date,datetime,timedelta
from   odoo import models,fields,api

class student(models.Model):
    _name='students.managment'
    _description='Student Description'

    first_name=fields.Char(string='First name',required=1)
    last_name=fields.Char(string='Last name')
    birth_date = fields.Date(string='Date Of Birth', defult=date.today())
    age = fields.Integer(string='Age', compute='_compute_age')

    subjects=fields.One2many('courses.managment','student_id',string='Subjects')

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            currentYear = date.today()
            if rec.birth_date:
                rec.age = currentYear.year - rec.birth_date.year
            else:
                rec.age = 18



