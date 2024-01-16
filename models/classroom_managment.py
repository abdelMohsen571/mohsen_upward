from odoo import api, fields, models, _, exceptions


class ClassroomManagment(models.Model):
    _name = 'classroom.managment'
    _description = '>>>>>>>>>>>>> '

    name = fields.Char(string='Class Name', required=1)
    student_id = fields.One2many('students.managment', 'classroom_id', string='Select Students')
    num_of_students = fields.Integer(string="Num Of Students", compute='_calac_num_of_students')

    @api.depends('student_id')
    def _calac_num_of_students(self):
        for rec in self:
            print(len(self.student_id))
            rec.num_of_students = len(self.student_id)

    @api.constrains('num_of_students')
    def check_num_of_students(self):
        for rec in self:
            if len(rec.student_id) > 4:
                raise exceptions.ValidationError(_("classroom is limited by 20 student"))
