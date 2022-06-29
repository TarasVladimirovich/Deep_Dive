class Person:
    name = "Adolf"
    age = "36"


print(type(Person))
print(type(type))
print(type(Person()))
q = Person

print(q.age)
print(q.name)
print(q.__class__)
print(q.__name__)
print(getattr(q, 'name'))

print(Person.__dict__)
print(q.__dict__)
print(dir(q))


class MyClass:
    __class__ = str


m = MyClass()
print(type(MyClass), MyClass.__class__, type(m), m.__class__)
