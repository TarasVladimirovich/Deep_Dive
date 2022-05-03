def my_func(a, b, /):
    return a + b


print(my_func(1, 2))


# print(my_func(a=1, b=2))

def my_func(a, b, /, *, c):
    return a + b + c


print(my_func(1, 2, c=3))

a, b = 'hello', 'world'
print(f'{a=:s} {b=}')
