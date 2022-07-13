class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    FULL = '{}.{}.{}'.format(MAJOR, MINOR, REVISION)


print(Language.FULL)


class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4

    @property
    def version(self):
        return '{}.{}.{}'.format(self.MAJOR, self.MINOR, self.REVISION)

    @classmethod
    def cls_version(cls):
        return '{}.{}.{}'.format(cls.MAJOR, cls.MINOR, cls.REVISION)

    @staticmethod
    def static_version():
        return '{}.{}.{}'.format(Language.MAJOR, Language.MINOR,
                                 Language.REVISION)


l = Language()
print(l.version)
print(l.cls_version())
print(l.static_version())
l.MAJOR = 4188
print(l.version)
print(l.cls_version())
print(l.static_version())


class Foo:
    counter = 0

    def __init__(self):
        Foo.counter += 1
        self.counter = 0

    def q(self):
        print(self.counter)

    @classmethod
    def w(cls):
        print(cls.counter)

    @staticmethod
    def e():
        print(Foo.counter)


Foo()
Foo()
Foo()
q = Foo()
print(Foo.counter)
q.q()
q.w()
q.e()
print(Foo.counter)
print(Foo.w)

name = 'Guido'


class MyClass:
    name = 'Raymond'
    list_1 = [name] * 3
    list_2 = [name.upper() for i in range(3)]

    @classmethod
    def hello(cls):
        return '{} says hello'.format(name)


print(MyClass.list_1)
MyClass.hello()
print(MyClass.list_2)
