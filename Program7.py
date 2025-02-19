# Write a program to calculate  area of rectangle using class & object concept

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

rect = Rectangle(10, 20)
print("Area of rectangle: ", rect.area())