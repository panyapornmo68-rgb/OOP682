from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def resize(self, new_width, new_height):
        pass
    def area(self):
        pass


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

def resize(shape, new_width, new_height):
    shape.resize(new_width, new_height)
    return shape.area()

rect = Rectangle(2, 3)
resize(rect, 4, 5)
print("Rectangle area:", rect.area())
square = Square(4)
resize(square, 4, 5)