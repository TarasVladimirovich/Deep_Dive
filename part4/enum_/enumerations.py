"""
https://peps.python.org/pep-0435/
"""
import enum


class Color(enum.Enum):
    red = 1
    green = 2
    blue = 3


class Status(enum.Enum):
    PENDING = 'pending'
    RUNNING = 'running'
    COMPLETED = 'completed'


class UnitVector(enum.Enum):
    V1D = (1,)
    V2D = (1, 1)
    V3D = (1, 1, 1)


print(Status.PENDING)
print(type(Status.PENDING))
print(isinstance(Status.PENDING, Status))
print(Status.PENDING.name, Status.PENDING.value)
print(Status.PENDING is Status.PENDING)
print(Status.PENDING == Status.PENDING)


class Constants(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3


try:
    Constants.ONE > Constants.TWO
except TypeError as ex:
    print(ex)

print(Status.PENDING in Status)
print(Status.PENDING.name, Status.PENDING.value)
# print('PENDING' in Status, 'pending' in Status)
print(Status('pending'), UnitVector((1, 1)))
try:
    Status('invalid')
except ValueError as ex:
    print(ex)


class Person:
    def __getitem__(self, val):
        return f'__getitem__({val}) called...'


p = Person()
print(p['some value'])

print(hasattr(Status, '__getitem__'))
print(Status['PENDING'])
print(getattr(Status, 'PENDING'))


class Person:
    __hash__ = None


p = Person()
try:
    hash(p)
except TypeError as ex:
    print(ex)


class Family(enum.Enum):
    person_1 = Person()
    person_2 = Person()


print(Family.person_1)
q = {
    Family.person_1: 'person 1',
    Family.person_2: 'person 2'
}

print(hasattr(Status, '__iter__'))

for member in Status:
    print(repr(member))


class Numbers1(enum.Enum):
    ONE = 1
    TWO = 2
    THREE = 3


class Numbers2(enum.Enum):
    THREE = 3
    TWO = 2
    ONE = 1


print(list(Numbers1), list(Numbers2))

try:
    Status.PENDING.value = 10
except AttributeError as ex:
    print(ex)

try:
    Status['NEW'] = 100
except TypeError as ex:
    print(ex)


class EnumBase(enum.Enum):
    pass


class EnumExt(EnumBase):
    ONE = 1
    TWO = 2


try:
    class EnumExt(EnumBase):
        TWO = 2
except TypeError as ex:
    print(ex)

import json

payload = """
{
  "name": "Alex",
  "status": "PENDING"
}
"""
data = json.loads(payload)
print(data['status'])
print(Status[data['status']])


def is_member(en, name):
    try:
        en[name]
    except KeyError:
        return False
    return True


print(is_member(Status, 'PENDING'))
print(is_member(Status, 'pending'))
print(getattr(Status, 'PENDING', None), getattr(Status, 'OK', None))
print(Status.__members__)

print('PENDING' in Status.__members__)