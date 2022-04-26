def f1():
    raise IndexError


def f2():
    return


def f3():
    raise SyntaxError


counters = []
for func in (f1, f2, f3):
    counter = 0
    try:
        try:
            func()
        except IndexError:
            counter += 1
        except SyntaxError:
            counter += 1
    finally:
        counter += 1
    counters.append(counter)
print(counters)

class A:
    def message(self):
        print('1', end='')

    def __enter__(self):
        print('2', end='')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('3', end='')
        else:
            print('4', end='')
            return True


with A() as action:
    action.message()

class Greeting:
    def __init__(self, param):
        self.__greeting = "Hello " + param
        print("Base__init__")


class Inherited(Greeting):
    # def __init__(self, param):
    #     print("Inherited__init__")
    def a(self):
        print("Inherited_a")
        print(self.__greeting)


obj = Inherited('Dear')
obj.a()  # "Hello Dear"


def outer(x):
    return lambda y: x + y
print(outer(5)(4))
