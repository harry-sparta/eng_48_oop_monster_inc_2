# Run 2. User-set run file
from monster_inc_staff import *
from monster_inc_student import *
from monster_inc_workshop import *
from monster_inc_lecture_theatre import *

## Set-up
    ### University
university = Uni('Monster Inc University')  # Uni class
    ### Building
building_1 = Building(university.uni_name,'Bloody Tower')
building_2 = Building(university.uni_name, 'Spooky Swamp Building')
    ### Lecture theatre
lecture_theatre_1 = Lecture_theatre(university.uni_name, building_1.building_name, 'Bloody theatre 1')
lecture_theatre_2 = Lecture_theatre(university.uni_name, building_1.building_name, 'Bloody theatre 2')
lecture_theatre_3 = Lecture_theatre(university.uni_name, building_2.building_name, 'Spooky theatre 1')
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

## While loop to temporarily simulate Uni Admin task