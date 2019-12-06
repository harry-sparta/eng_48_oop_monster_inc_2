# Inherits from Uni()
# Child class - inherits from Uni
from monster_inc_uni import *

class Building(Uni):
    # define attributes
    def __init__(self, uni_name, building_name):
        super().__init__(uni_name)
        self.building_name = building_name
    pass

    # define behaviors