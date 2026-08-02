class Person:
    def __init__(self, name = None, age = None, gender = None, occupation = None):
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
    def set_attributes(self, attributes):
        for key, value in attributes.items():
            setattr(self, key, value)
    def show_card(self):
        print(f'''Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nOccupation: {self.occupation}''')