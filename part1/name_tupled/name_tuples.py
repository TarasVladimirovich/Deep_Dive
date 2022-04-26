from collections import namedtuple

PT = namedtuple('test', 'x y z')
q = PT(10, 20, 40)
print(q)

Point2D = namedtuple('Point2d', ('x', 'y'))
p2d = Point2D(2, 10)
print(p2d)
print(p2d[0])
print(p2d.x)
print(type(p2d))
print(type(Point2D))
Person = namedtuple('Person', 'name age')
print(Person._fields)
print(p2d._asdict())