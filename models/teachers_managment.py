from   odoo import models,fields,api
class TeachersManagment(models.Model):
    _name='teachers.managment'
    _description='Teachers Description'

    name = fields.Char(string='Name',required=1)
    age = fields.Integer(string="Age")
    desciption = fields.Html(string="Description")
    is_student = fields.Boolean(string="Is this ")
    gender = fields.Selection([("male", "Male"), ("femal", "Female")], string="Gender")
    upload_image = fields.Image(string="Upload Your Image")


