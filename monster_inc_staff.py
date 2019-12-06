# Child class - inherits from Monster and Uni
from monster_inc_uni import *
from monster_inc_monster import *

class Staff(Monster, Uni):
    # define attributes
    def __init__(self, uni_name, monster_name, monster_skills):
        Monster.__init__(self, monster_name, monster_skills) # using super to inherit default attribute from Monster
        Uni.__init__(self, uni_name)  # using super to inherit default attribute from Uni. Can't inherit two classes in one super

    pass

    # Define behaviors

