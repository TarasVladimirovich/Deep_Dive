def outer():
    x = 'python'

    def inner():
        print(x)

    return inner


fn = outer()
print(fn.__closure__)
print(fn.__code__.co_freevars)