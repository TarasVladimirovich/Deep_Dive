from marshmallow import Schema, fields, post_load


class Person:
    def __init__(self, first_name, last_name, dob, height):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.height = height

    def __repr__(self):
        return f'Person({self.first_name}, {self.last_name}, {self.dob})'


class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()
    height = fields.Int()

    @post_load
    def make_person(self, data, **kwargs):
        return Person(**data)


d = {"first_name": "John", "last_name": "Cleese", "dob": "1939-10-27", "height": 188}
person_schema = PersonSchema()

print(person_schema.load(d))
