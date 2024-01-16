from   odoo import models,fields,api,_
from datetime import date,datetime
from odoo.exceptions import ValidationError
class TeachersManagment(models.Model):
    _name='teachers.managment'
    _description='Teachers Description'

    name = fields.Char(string='Name',required=1)
    age = fields.Integer(string="Age")
    desciption = fields.Html(string="Description")
    is_student = fields.Boolean(string="Is this ")
    gender = fields.Selection([("male", "Male"), ("femal", "Female")], string="Gender")
    joning_date = fields.Date(string='Joninig Date',defult=date.today())
    years_of_experience = fields.Integer(string='Years Of Experience', compute='_compute_experience')

    upload_image = fields.Image(string="Upload Your Image")

    # sql_constraints = [('check_age','1=1','age should be grater than 6'),]


    @api.constrains('age')
    def check_age(self):
        if self.age<6:
            raise ValidationError(_('Age Can not be less than 6'))

    @api.depends('joning_date')
    def _compute_experience(self):
        for rec in self:
            experience_year = date.today()
            if rec.joning_date:
                rec.years_of_experience = experience_year.year - rec.joning_date.year
            else:
                rec.years_of_experience = 0


