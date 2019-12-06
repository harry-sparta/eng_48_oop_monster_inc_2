# Inherits from campus
# Child class - inherits from Campus
from monster_inc_building import *

class Lecture_theatre(Building):
    # define attributes
    def __init__(self, uni_name, building_name, lecture_theatre_name):
        super().__init__(uni_name, building_name)
        self.lecture_theatre_name = lecture_theatre_name
    pass

    # define behaviors


    ## if same method in parent class
    ## using super().method can add additional method outputs to the default output