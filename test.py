# Test file
## import from py files
from monster_inc_staff import *
from monster_inc_student import *
from monster_inc_workshop import *


## T.0 Testing setup
university = Uni('Monster Inc University')  # Uni class
monster_1 = Monster('Paul',['scream','jump','curl up']) # Monster class
monster_2 = Staff(university.uni_name, 'Prof. Mike', ['bounce', 'shout', 'clap'], 'STAFF0001') # Staff class
monster_3 = Student(university.uni_name, 'Stud. Jay', ['sing', 'shave', 'dance'], 'S0007', 'A+')   # Student class
monster_4 = Student(university.uni_name, 'Stud. Venice', ['roll', 'sleep', 'spit'], 'S0008', 'B-')   # Student class
workshop_1 = Workshop(university.uni_name, 'Scare 101')

### T.1) uni name
print('T.1) Test if Uni class attribute name is equal to: Monster Inc Unversity')
print('    Result: ', university.uni_name == 'Monster Inc University', '    Output: ', university.uni_name)

### T.2.1) monster name
print('\nT.2.1) Test if monster class attribute name is equal to: Paul')
print('    Result: ', monster_1.monster_name == 'Paul', '    Output: ', monster_1.monster_name)

### T.2.2) monster skills
print('\nT.2.1) Test if monster class attribute skills is equal to: [scream, jump, curl up]')
print('    Result: ', monster_1.monster_skills == ['scream','jump','curl up'], '   Output: ', monster_1.monster_skills)

### T.3.1) staff default attribute name from monsters
print('\nT.3.1) Test if monster class attribute name is equal to: Prof. Mike')
print('    Result: ', monster_2.monster_name == 'Prof. Mike', '   Output: ', monster_2.monster_name)

### T.3.2) staff default attribute skills from monsters
print('\nT.3.2) Test if monster class attribute skills is equal to: [bounce, shout, clap]')
print('    Result: ', monster_2.monster_skills == ['bounce', 'shout', 'clap'], '   Output: ', monster_2.monster_skills)

### T.3.3) staff default attribute uni_name from uni
print('\nT.3.3) Test if Uni class attribute uni_name is equal to: Monster Inc University')
print('    Result: ', monster_2.uni_name == 'Monster Inc University', '   Output: ', monster_2.uni_name)

### T.4.1) student default attribute name from monsters
print('\nT.4.1) Test if monster class attribute name is equal to: Stud. Jay')
print('    Result: ', monster_3.monster_name == 'Stud. Jay', '   Output: ', monster_3.monster_name)

### T.4.2) student id from student
print('\nT.4.2) Test if student class attribute id is equal to: S0007')
print('    Result: ', monster_3.student_id == 'S0007', '   Output: ', monster_3.student_id)

### T.4.3) Student default attribute uni_name from uni
print('\nT.4.3) Test if student class attribute uni_name is equal to: Monster Inc University')
print('    Result: ', monster_3.uni_name == 'Monster Inc University', '   Output: ', monster_3.uni_name)

### T.4.4) Student attribute grade
print('\nT.4.4) Test if student class attribute grade is equal to: A+')
print('    Result: ', monster_3.see_grade() == 'A+', '   Output: ', monster_3.see_grade())

### T.4.5) Student set attribute grade
print('\nT.4.5) Test if student class attribute grade can change from A+ to C-')
monster_3.set_grade('C-')
print('    Result: ', monster_3.see_grade() == 'C-', '   Output: ', monster_3.see_grade())

### T.5.1) Workshop class attribute subject
print('\nT.5.1) Test if Workshop class attribute subject is equal to: Scare 101')
print('    Result: ', workshop_1.subject == 'Scare 101', '   Output: ', workshop_1.subject)

### T.5.2) Workshop class behavior add a student
print('\nT.5.2) Test if workshop class behavior add_student is equal to: [S0007]')
workshop_1.add_student(monster_3.student_id)
print('    Result: ', workshop_1.enrollment_student == ['S0007'], '   Output: ',
      workshop_1.enrollment_student)

### T.5.3) Workshop class behavior add a staff
print('\nT.5.3) Test if workshop class behavior add_staff is equal to: [STAFF0001]')
workshop_1.add_staff(monster_2.staff_id)
print('    Result: ', workshop_1.enrollment_staff == ['STAFF0001'], '   Output: ',
      workshop_1.enrollment_staff)

