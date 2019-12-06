# Child class - inherits from Monster and Uni
from monster_inc_uni import *
from monster_inc_monster import *

class student(Monster, Uni):
    # define attributes
    def __init__(self, uni_name, monster_name, monster_skills, student_id, grade):
        Monster.__init__(self, monster_name, monster_skills) # Multiple inheritance from Monster and Uni classes
        Uni.__init__(self, uni_name)
        self.student_id = student_id
        self.grade = grade
    pass

    # define behaviors