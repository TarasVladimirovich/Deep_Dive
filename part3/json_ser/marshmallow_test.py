from datetime import date, datetime
from collections import namedtuple

from marshmallow import Schema, fields


class Person:
    def __init__(self, first_name, last_name, dob, height):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.height = height

    def __repr__(self):
        return f'Person({self.first_name}, {self.last_name}, {self.dob})'


p1 = Person('John', 'Cleese', date(1939, 10, 27), 188)
print(p1)


class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()
    height = fields.Int()


person_schema = PersonSchema()
q = person_schema.dump(p1)
data = person_schema.dumps(p1)
print(type(q), q)
print(type(data), data)

PT = namedtuple('PT', 'first_name, last_name, dob, height')

p2 = PT('ERIK', 'TAKKOE', date(1939, 10, 27), 148)
print(type(p2), p2)

print('*' * 100)
data = person_schema.dumps(p2)
print(type(q), q)
print(type(data), data)

PT2 = namedtuple('PT2', 'first_name, last_name, age')
p3 = PT2('One', 'Two', 34)
print('*' * 100)
print(person_schema.dumps(p3), 'Partial dump, that schema know ')
print('*' * 100)

person_partial = PersonSchema(only=('first_name', 'last_name'))
print(person_partial.dumps(p1), 'partial dump that we mentioned in ONLY')
print(person_schema.dumps(p1))
print('*' * 100)
person_partial = PersonSchema(exclude=['dob'])
print(person_partial.dumps(p1), 'partial dump that we exclude in exclude')

# p4 = Person(100, None, 200, 'abc')
# print(person_schema.dumps(p4)) Error
