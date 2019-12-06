# Run file
from monster_inc_staff import *
from monster_inc_student import *
from monster_inc_workshop import *

## Set-up
    ### University
university = Uni('Monster Inc University')  # Uni class
    ### Student
monster_1 = Student(university.uni_name, 'Jane', ['scream', 'jump', 'snore'], 'S0001', 'TBC')
monster_2 = Student(university.uni_name, 'Mike', ['bounce', 'shout', 'clap'], 'S0002', 'TBC')
monster_3 = Student(university.uni_name, 'Barbara', ['sing', 'shave', 'dance'], 'S0003', 'TBC')
    ### Staff
monster_4 = Staff(university.uni_name, 'Prof. Chutney', ['slap', 'creep', 'high-five'], 'T0001')
monster_5 = Staff(university.uni_name, 'Prof. Armless', ['smile', 'spit', 'stare'], 'T0002')
    ### Workshop
workshop_1 = Workshop(university.uni_name, 'Scary 101')
workshop_2 = Workshop(university.uni_name, 'Spooky 101')
workshop_3 = Workshop(university.uni_name, 'Creepy 101')



##