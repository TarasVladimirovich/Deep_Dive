class Shape:
    pass


class Ellipse(Shape):
    pass


class Circle(Shape):
    pass


class Polygon(Shape):
    pass


class Rectangle(Polygon):
    pass


class Square(Rectangle):
    pass


class Triangle(Polygon):
    pass


print(issubclass(Ellipse, Shape))
print(issubclass(Circle, Shape))

s = Shape()
e = Circle()
sq = Square()
p = Polygon()
print(isinstance(s, Shape))
print(isinstance(sq, Rectangle))
print(isinstance(sq, Shape))
print(isinstance(sq, Ellipse))
print("TYPE = ", isinstance(sq, type(p)))
print("issubclass = ", issubclass(type(sq), type(p)))
print(type(sq))
print(type(Shape))

import math

print(type(math))
import types
print(dir(types))