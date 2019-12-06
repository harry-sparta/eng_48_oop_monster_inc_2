# Inherits from Uni()
from monster_inc_uni import *

class Workshop(Uni):
    # define attributes
    def __init__(self, subject, enrollment_staff, enrollment_student):
        self.subject = subject
        self.enrollment_staff = enrollment_staff
        self.enrollment_student = enrollment_student
    pass

    # define behaviors
