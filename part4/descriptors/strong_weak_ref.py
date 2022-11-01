import ctypes
import weakref


def ref_count(address):
    return ctypes.c_long.from_address(address).value


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person(name={self.name})'


p1 = Person('Guido')
p2 = p1

p1_id = id(p1)
p2_id = id(p2)

print(p1_id == p2_id, ref_count(p1_id))
del p2
print(ref_count(p1_id))
del p1
print(ref_count(p1_id))

p1 = Person('Guido')
p1_id = id(p1)
print(ref_count(p1_id))
p2 = p1
print(ref_count(p1_id))
weak1 = weakref.ref(p1)
print(ref_count(p1_id))
print(hex(p1_id))
print(weak1)
print(weak1 is p1)
print(weak1() is p1)
print(p1.__weakref__)