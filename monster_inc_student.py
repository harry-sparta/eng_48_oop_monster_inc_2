# Child class - inherits from Monster and Uni
from monster_inc_uni import *
from monster_inc_monster import *

class Student(Monster, Uni):
    # define attributes
    def __init__(self, uni_name, monster_name, monster_skills, student_id, grade):
        Monster.__init__(self, monster_name, monster_skills) # Multiple inheritance from Monster and Uni classes
        Uni.__init__(self, uni_name)
        self.student_id = student_id
        self.__grade = grade  # encapsulate student grades
    pass

    # define behaviors
    ## get student grade
    def see_grade(self):    # Getter
        return self.__grade

    ## set student grade
    def set_grade(self, grade):     # Setter
        self.__grade = grade
