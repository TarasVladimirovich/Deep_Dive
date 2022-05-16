import json

d1 = {'a': 100, 'b': 200}
d1_json = json.dumps(d1)
print(d1_json)
print(type(d1_json))
d1_json = json.dumps(d1, indent=2)
print(d1_json)
d2 = json.loads(d1_json)
print(d2)
print(type(d2))
print(d1 == d2)
print(d1 is d2)

d11 = {1: 100, 2: 200}
d11_json = json.dumps(d11)
print(d11)
print(d1_json)
d22 = json.loads(d11_json)
print(d22)
print(d11 == d22)
print(d11 is d22)


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def toJSON(self):
        return vars(self)


p = Person('Ivan', 36)
# p.platform = 'test'
print(p.toJSON())
print(json.dumps({'ivan': p.toJSON()}, indent=2))

