# Run 1. Pre-set run file
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

### Running scenario
print('###############'+ ' WELCOME TO ' + university.uni_name.upper() + ' ###################')
print('\n-------------------Workshops currently available-------------------')
print(workshop_1.subject, '\n' + workshop_2.subject, '\n' + workshop_3.subject)   # Listing workshops available
print('\n----Currently no student or staff are enrolled in any work shops----')
print('Student (ids) currently in', workshop_1.subject, ': ', workshop_1.enrollment_student)    # showing student list
print('Staff (ids) currently in', workshop_1.subject, ': ', workshop_1.enrollment_staff)    # showing staff list
print('Lecture theatre for the workshop Scary 101 is in: ', workshop_1.lecture_theatre) # showing lecture theatre
print('\n----------With student and staff enrolled into Scary 101-------------')
workshop_1.add_student(monster_1.student_id)    # Enrolling monster_1 (student) into Scary 101
workshop_1.add_student(monster_2.student_id)    # Enrolling monster_2 (student) into Scary 101
workshop_1.add_staff(monster_4.staff_id)    # Enrolling monster_4 (staff) into Scary 101
print('Student (ids) currently in', workshop_1.subject, ':')    # showing student list
for student_id in workshop_1.enrollment_student:
    print(student_id)
print('\nStaff (ids) currently in', workshop_1.subject, ':')    # showing staff list
for staff_id in workshop_1.enrollment_staff:
    print(staff_id)
print('\n------------- With a lecture theatre added to Scary 101--------------')
workshop_1.add_lecture_theatre(lecture_theatre_1.lecture_theatre_name)   # Adding a lecture theatre to Scary 101
print('Lecture theatre for the workshop Scary 101 is in: ') # showing lecture theatre
for theatre_name in workshop_1.lecture_theatre:
    print(theatre_name)
print('\n------------ Grading students enrolled on to Scary 101 ---------------')
monster_1.set_grade('A')
monster_2.set_grade('B')
print('Inform monster_1 (student) with student_id', monster_1.student_id, 'its grade is', monster_1.see_grade())
print('\n########################## THANK YOU #################################')