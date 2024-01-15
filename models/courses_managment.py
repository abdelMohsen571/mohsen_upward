from wheel.metadata import requires_to_requires_dist

from odoo import api,fields,models
class CoursesManagment(models.Model):
    _name='courses.managment'
    _rec_name = "lectures9o`"
    _description='Course that the students should enroll in it '



    name_f=fields.Char(string='Course Name' ,required=1)
    lectures=fields.Char(string='Num of Licture')
    teacher_id=fields.Many2one('teachers.managment',string='Instructor')
    hours=fields.Float(sring='courses hours',digits='4digit', help='how many hours for this course')
    student_id=fields.Many2one('students.managment',string='Select Students')

