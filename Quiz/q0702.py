"""
© https://sudipghimire.com.np
Create a class named Person and add the following attributes and methods:
- name:     Instance attribute
- age:      Instance attribute
- gender:   Instance attribute
- weight:   Class attribute
- year_of_birth():
Returns the year by subtracting the age from the current year.
- get_pronouns():
Returns list of ['he', 'his', 'him'] or ['she', 'her', 'hers'] by checking the gender
the initializer method should take name, age, and gender
"""
#%%
import datetime

current_year = datetime.date.today().year

class Person:
    weight = 0
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def year_of_birth(self):
        return f'Year of birth is {current_year-self.age}'
    def get_pronouns(self):
        male = ['he', 'his', 'him']
        female = ['she', 'her', 'hers']
        if self.gender in male:
            print(f' pronouns are {male}')                     
        return f' Pronouns are {female}'


ram = Person("Ram", 21, "male")
print(ram.year_of_birth())
print(ram.get_pronouns())

print()

sita = Person("Sita",98, "female" )
print(sita.year_of_birth())
print(sita.get_pronouns())
                            
#%%
