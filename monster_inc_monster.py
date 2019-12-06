# Top class - no inheritance
class Monster():
    # define attributes
    def __init__(self, monster_name, monster_skills): # Run when you create an object
        self.monster_name = monster_name
        self.monster_skills = monster_skills
    pass

    # Define behaviors
    def add_skills(self, new_skills):
        self.monster_skills.append(new_skills)

