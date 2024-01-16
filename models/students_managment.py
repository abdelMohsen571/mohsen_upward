from datetime import date,datetime,timedelta
from   odoo import models,fields,api

class student(models.Model):
    _name='students.managment'
    _description='Student Description'

    first_name=fields.Char(string='First name',required=1)
    last_name=fields.Char(string='Last name')
    birth_date = fields.Date(string='Date Of Birth', defult=date.today())
    age = fields.Integer(string='Age')
    classroom_id=fields.Many2one('classroom.managment',string='Classrooom')
    # num_of_subjects=fields.Integer(string="Num Of Students")
    #
    # @api.depends('birth_date')
    # def _compute_age(self):
    #     for rec in self:
    #         currentYear = date.today()
    #         if rec.birth_date:
    #             rec.age = currentYear.year - rec.birth_date.year
    #         else:
    #             rec.age = 18


    # _sql_constraints = [('check_age','1=1','age should be grater than 6')]





