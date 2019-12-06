# Test file
## import from py files
from monster_inc_staff import *


## T.0 Testing setup
universiy = Uni('Monster Inc University')  # Uni class
monster_1 = Monster('Paul',['scream','jump','curl up']) # Monster class
monster_2 = Staff(universiy.uni_name,'Prof. Mike',['bounce', 'shout', 'clap']) # Monster & Staff class
# monster_3 = Student()

### T.1) uni name
print('T.1) Test if Uni class attribute name is equal to: Monster Inc Unversity')
print('    Result: ', universiy.uni_name == 'Monster Inc University', '    Output: ', universiy.uni_name)

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