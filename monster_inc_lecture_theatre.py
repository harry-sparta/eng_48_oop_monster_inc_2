# Inherits from campus
# Child class - inherits from Campus
from monster_inc_campus import *

class Lecture_theatre(Campus):
    # define attributes
    def __init__(self, uni_name, building, lecture_theatre_name):
        super().__init__(uni_name, building)
        self.lecture_theatre_name = lecture_theatre_name
    pass

    # define behaviors
    ## if same method in parent class
    ## using super().method can add additional method outputs to the default output