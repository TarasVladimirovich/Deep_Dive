class MyClass:
    language = 'Python'

    def say_hello():
        print('Hello')

    def foo(self):
        print(f'{self.language}')

    @classmethod
    def boo(cls):
        print(f'{cls.language}')


MyClass.boo()
MyClass().foo()
# MyClass.foo()

p = MyClass()
p.boo()
p.foo()
MyClass.say_hello()
print(MyClass.say_hello)
print(MyClass().say_hello)
print(p.say_hello)
