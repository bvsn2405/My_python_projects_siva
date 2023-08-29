# from abc import ABC, abstractmethod
from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @staticmethod
    def figure():
        return 'It is a 2D plane figure'


class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def sides(self):
        print('The Rectangle Parameters : ')
        print('-' * len('The Rectangle Parameters :'))
        return f'Length is : {self.length}\nBreadth is : {self.breadth}'

    def area(self):
        return f'Area is : {self.length * self.breadth}'

    def perimeter(self):
        return f'Perimeter is : {2 * (self.length + self.breadth)}'

    @staticmethod
    def extra_method():
        return "Rectangle has 4 sides"


class Triangle(Polygon):
    def __init__(self, breadth, height):
        self.breadth = breadth
        self.height = height

    def sides(self):
        print('The Triangle Parameters : ')
        print('-' * len('The Triangle Parameters :'))
        return f'Breadth is : {self.breadth}\nHeight is : {self.height}'

    def area(self):
        return f'Area is : {0.5 * self.breadth * self.height}'

    def perimeter(self):
        return f'Perimeter is : {3 * self.breadth}'

    @staticmethod
    def extra_method():
        return "Triangle has 3 sides"


class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def sides(self):
        print('The Square Parameters : ')
        print('-' * len('The Square Parameters :'))
        return f'Length of the side is : {self.side}'

    def area(self):
        return f'Area is : {self.side * self.side}'

    def perimeter(self):
        return f'Perimeter is : {4 * self.side}'

    @staticmethod
    def extra_method():
        return "Square has 4 sides"


if __name__ == '__main__':
    rect = Rectangle(10, 20)
    tri = Triangle(10, 20)
    sqr = Square(10)
    for obj in [rect, tri, sqr]:
        print(obj.sides())
        print(obj.area())
        print(obj.perimeter())
        print(obj.extra_method())
        print(obj.figure())
