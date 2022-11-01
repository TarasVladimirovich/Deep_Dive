class IntegerValue:
    def __set__(self, instance, value):
        instance.stored_value = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return getattr(instance, 'stored_value', None)


class Point1D:
    x = IntegerValue()


# p1, p2 = Point1D(), Point1D()
#
# p1.x = 10
# p2.x = 20
# print(p1.x, p2.x)
# print(p1.__dict__)
# print(p2.__dict__)


class Point2D:
    x = IntegerValue()
    y = IntegerValue()


# p = Point2D()
# p.x = 10.1
# p.y = 20.2
# print(p.__dict__)
# print(p.x, p.y)


class IntegerValue:
    def __init__(self, name):
        self.storage_name = '_' + name

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, int(value))

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)


class Point2D:
    x = IntegerValue('x')
    y = IntegerValue('y')


p1 = Point2D()
p2 = Point2D()


# p1.x = 10.1
# p1.y = 20.2
# print("*" * 10)
# print(p1.x, p1.y)
# print(p1.__dict__)
# print(p2.__dict__)
# p2.x = 100.1
# p2.y = 200.2
# print(p2.__dict__)


class IntegerValue:
    def __init__(self):
        self.values = {}

    def __set__(self, instance, value):
        self.values[instance] = int(value)

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return self.values.get(instance)


class Point2D:
    x = IntegerValue()
    y = IntegerValue()


p1 = Point2D()
p2 = Point2D()
print(Point2D.x.values)
p1.x = 10.1
p1.y = 20.2
p2.x = 100
p2.y = 200
print(p1.x, p1.y)
print(p2.x, p2.y)
print(Point2D.x.values)
print(Point2D.y.values)

import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value


p1 = Point2D()
id_p1 = id(p1)
print(ref_count(id_p1))
p1.x = 100.1
print(ref_count(id_p1))
print('p1' in globals())
del p1
print('p1' in globals())
print(ref_count(id_p1))
print(Point2D.x.values.items())
# issue with memory
print("5"*20)
# print(locals())
# print(globals())
# import gc
# print(gc.get_objects())
