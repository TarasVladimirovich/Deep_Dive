def outer():
    a = 100
    x = 'python'
    w = 1000

    def inner():
        a = 10
        print(f'{x} rocks!')
        print(f'{a}: A!')
        print(w)

    return inner


fn = outer()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(outer()())


def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc


f1 = counter()
f2 = counter()
print(id(f1))
print(id(f2))
print(f1())
print(f1())
print(f1())
print(f2())


# shared extended scopes
def counter1():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2


f1, f2 = counter1()
print(f1())
print(f2())
print(f1())
print(f2())
print(f1())
print(f2())

