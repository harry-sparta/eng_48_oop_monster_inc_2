# Inherits from Uni()
from monster_inc_uni import *

class Workshop(Uni):
    # define attributes
    def __init__(self, uni_name, subject):
        super().__init__(uni_name)
        self.subject = subject
        self.enrollment_student = []
        self.enrollment_staff = []
    pass

    # define behaviors
    ## method to add students in ids on a workshop
    def add_student(self, enrol_student):
        self.enrollment_student.append(enrol_student)

    ## method to add staff in ids on a workshop
    def add_staff(self, enrol_staff):
        self.enrollment_staff.append(enrol_staff)

