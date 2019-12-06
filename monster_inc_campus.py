# Inherits from Uni()
# Child class - inherits from Uni
from monster_inc_uni import *

class Campus(Uni):
    # define attributes
    def __init__(self, uni_name, building):
        super().__init__(uni_name)
        self.building = building
    pass

    # define behaviors