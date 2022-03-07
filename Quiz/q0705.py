"""://sudipghimire.com.np
create a classes Rectangle, Circle and Box and add respective attributes eg.: radius, length, width, height
for Rectangle, create methods to find out:
    perimeter
    area
    length of diagonal
for Circle, create methods to find out:
    circumference
    area
    diameter
for Box, create methods to find out:
    surface area
    volume
"""

# answer
#%%


#from curses.textpad import rectangle
from operator import length_hint
from turtle import width
from xml.etree.ElementTree import PI


class Rectangle:
    length = 0
    width  = 0
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_rectangle(self):
        return f'Area of the rectangle is : {self.length * self.width}'
    
    def perimeter_rectangle(self):
        return f'Perimeter of the rectangle is: {2*(self.length + self.width)}'

    def length_of_daigonal_of_rectangle(self):
        return f'Length of the diagnol of the rectangle is: {(self.length**2 + self.width**2)**0.5}'

rec = Rectangle(4,3)
print(rec.area_rectangle())
print(rec.perimeter_rectangle())
print(rec.length_of_daigonal_of_rectangle())

#%%

class Circle:
    radius = 0
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return f' Area of the circle is: {self.PI*self.radius**2}'
    
    def circumference(self):
        return f'Circumference of the circle is: {2*self.PI*self.radius}'

    def diameter(self):
        return f'Diameter of the circle is: {2*self.radius}'

cir = Circle(10)
print(cir.area())
print(cir.circumference())
print(cir.diameter())

#%%

class Box:
    length = 0
    width = 0
    height = 0

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self):
        return f'Surface area of the box is: {2*(self.length*self.width + self.width*self.height + self.length*self.height)}'

    def volume (self):
        return f'Volume of the box is: {self.length * self.width * self.height}'

box = Box(10,20,30)
print(box.surface_area())
print(box.volume())

#%%