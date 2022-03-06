"""
© https://sudipghimire.com.np
Create a class Employee that contains different attributes.
- id
- first_name
- last_name
- project
- department
- salary
Make attributes project, department, and salary as private and use getter and setter methods to get and
set respective values
id should be private and can only be initialized when employee instance is created
first_name and last_name should be initialized with constructor and can be changed any time
"""

# answer
#%%


from tkinter import CENTER


class Employee:
    __project = ""
    __department = ""
    __salary = 0
    __id = ""

    def __init__(self, first_name, last_name, id, department, project, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.__id = id
        self.__department = department
        self.__project = project
        self.__salary  = salary
    # Getter method
    def get_employee_id(self):
        return f' His/Her EID is: {self.__id}'
    # Getter method
    def get_project(self):
        return f' His/Her porject name is : {self.__project}'
    # Getter method
    def get_department(self):
        return f' His/Her department name is : {self.__department}'
    # Getter method
    def get_salary(self):
        return f' His/Her salary is : {self.__salary}'
    # Setter method
    def set_department(self, department):
        self.__department = department
    # Setter method
    def set_project(self, project):
        self.__project = project
    # Setter method
    def set_salary(self, salary):
        self.__salary = salary
    
   

Kushal = Employee("Kushal", "Niraula","DA001","Data Analytics","Machine learning",140000)
print("Initail Information of candidate: ".center(80))
print(Kushal.get_department())
print(Kushal.get_project())
print(Kushal.get_salary())
print(Kushal.get_employee_id())

Kushal.set_department("Data Science")
Kushal.set_project("Artificial Inteligence")
Kushal.set_salary(200000)
#Kushal.set_employee_id ("AB005") # has not defined and not able to change it.

print("\n Information of candidate after setting new attributes:\n ".center(80))
print(Kushal.get_department())
print(Kushal.get_project())
print(Kushal.get_salary())
print(Kushal.get_employee_id()) # will print old EID



#%%