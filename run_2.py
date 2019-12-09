# Run 2. User-set run file
from monster_inc_staff import *
from monster_inc_student import *
from monster_inc_workshop import *
from monster_inc_lecture_theatre import *

## Set-up

## Creating a university
new_uni_name = input('Enter a University name: (name)    ')
new_uni = Uni(new_uni_name)
print('UNIVERSITY NAME: ', new_uni.uni_name)



## Workshop list
workshop_list = []

while True:
    print('Choose an command:', '\n"1" - User manual', '\n"2" - See workshop list',
          '\n"3" - Create Uni monster membership', '\n"4" Create new workshop',
          '\n"5" Print full monster membership information')
    command = input('Enter a command to navigate to:    ')
    if command == '1':
        print('>> Accessing "User manual" ')
        print('Manual TBC')

    elif command == '2':
        # Prints workshop list or 'No workshop'
        print('>> Accessing "See workshop list" ')
        if not workshop_list:
            print('Currently no workshop enlisted')
        else:
            print('Current workshop list')
            counter = 0
            for workshop in workshop_list:
                print('"'+str(counter)+'"', '-', workshop.subject)
                counter += 1
            # Prompt user for workshop to access for further commands
            workshop_list_command = input('Which workshop would you like to access, enter a command (number): ')
            user_chosen_workshop = workshop_list[int(workshop_list_command)]
            print('>> Accessing "See workshop list" >> "Workshop: "', user_chosen_workshop.subject)
            print('Choose an command:', '\n"1" - See enrollment list', '\n"2" - Add student_id to workshop',
                  '\n"3" - Add staff_id to workshop')
            workshop_list_inside_command = input('Enter a command (number): ')
            if workshop_list_inside_command == "1":
                if not user_chosen_workshop.enrollment_student:
                    print('no enrollment')
                else:
                    for student_id in user_chosen_workshop.enrollment_student:
                        print(student_id)
                    for staff_id in user_chosen_workshop.enrollment_staff:
                        print(staff_id)
            elif workshop_list_inside_command == "2":
                user_add_student = input('Enter a student id to add to workshop:    ')
                user_chosen_workshop.add_student(user_add_student)
            elif workshop_list_inside_command == "3":
                user_add_staff = input('Enter a staff id to add to workshop:    ')
                user_chosen_workshop.add_student(user_add_staff)

    elif command == '3':
        # Create a monster
        print('>> Accessing "Create a monster" ')
        print('"1" - student', '\n"2" - staff')
        user_new_monster = input('Choose a monster type, enter a command (number):    ')
        student_num = 0
        staff_num = 0
        if user_new_monster == "1":
            new_student_name = input('Enter a new monster name: (name)   ')
            new_student_skills = input('Enter a new monster skill: (skill 1, skill 2, skill 3.....etc)   ')
            new_student_id = input('Enter a student id:   ')
            new_student_grade = input('Enter a grade:     ')
            new_student = Student(new_uni.uni_name, new_student_name,new_student_skills,new_student_id,new_student_grade)
            print('NAME: ', new_student.monster_name, '\nSKILLS: ', new_student.monster_skills,
                  '\nSTUDENT ID: ', new_student.student_id,'\nGRADE: ', new_student.see_grade())
        elif user_new_monster == "2":
            new_staff_name = input('Enter a new monster name: (name)   ')
            new_staff_skills = input('Enter a new monster skill: (skill 1, skill 2, skill 3.....etc)   ')
            new_staff_id = input('Enter a staff id:   ')
            new_staff = Staff(new_uni.uni_name, new_staff_name,new_staff_skills,new_staff_id)
            print('NAME: ', new_staff.monster_name, '\nSKILLS: ', new_staff.monster_skills,
                  '\nSTAFF ID: ', new_staff.staff_id)

    elif command == '4':
        print('>> Accessing "Create a new workshop" ')
        # Creating a new workshop
        new_workshop_1_subject = input('Enter a subject: (subject)   ')
        new_workshop_1 = Workshop(new_uni.uni_name, new_workshop_1_subject)
        print('NEW SUBJECT CREATED: ', new_workshop_1_subject)
        workshop_list.append(new_workshop_1)

    elif command == '5':
        print('NAME:      ', new_student.monster_name,'\n      SKILLS: ',new_student.monster_skills,'      Grade: ',
              new_student.see_grade())
        print('NAME:      ', new_staff.monster_name,'\n      SKILLS: ',new_staff.monster_skills)




