"""
© https://sudipghimire.com.np
Create a python class with following properties:
1. private class attribute
2. public class attribute
3. instance attribute
4. initializer method
5. string representation method [__str__()]
"""

# Your solution here
#%%
class HouseModel:
    style = ""              # class attribute
    material = ""           # class attribute
    __room = 0              # private class attribute
    _garage = 0             # protected class atrribute

    def __init__(self, style, material, floor):         # initializer method                                      
        self.style = style
        self.material = material
        self.floor = floor                             # instance attribute
    
    def describe(self):                                 # string represention method
        return f'My house style is {self.style} and has {self.floor} floor.'


my_house = HouseModel("Sweet","wood", 2)

print (my_house.describe())


#%%