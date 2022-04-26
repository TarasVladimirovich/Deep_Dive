from itertools import compress, takewhile, dropwhile, filterfalse
from math import sin, pi

print(*filter(lambda x: x < 4, [1, 2, 4, 12, 4, 35, 5, 56, 2, 3, 1]))
print(*filter(None, [0, '', 'hello', 100, [], False]))
print(*filter(None, [0, '', 'hello', 100, [], False]))  # Look at True values


# filter returns lazy iterators
# compress, takewhile, dropwhile returns lazy iterators

def get_cube(n):
    for i in range(n):
        # print(f'yielding {i}')
        yield i ** 3


def is_odd(x):
    return x % 2 == 1


def is_even(x):
    return x % 2 == 0


filtered = list(filter(is_odd, get_cube(10)))
filtered_even = list(filter(is_even, get_cube(10)))
print(f'filtered_odd={filtered}')
print(f'filtered_even={filtered_even}')
filtered = list(filterfalse(is_odd, get_cube(10)))
filtered_even = list(filterfalse(is_even, get_cube(10)))
print(f'filtered_even_false={filtered}')
print(f'filtered_odd_false={filtered_even}')


## dropwhhile takewgile
def sine_wave(n):
    start = 0
    max_ = 2 * pi
    step = (max_ - start) / (n - 1)
    for _ in range(n):
        yield round(sin(start), 2)
        start += step


print(*sine_wave(15))
print(*takewhile(lambda x: 0 <= x <= 0.9, sine_wave(15)))
l = [1, 3, 5, 2, 1]
print(*dropwhile(lambda x: x < 5, l))

## compress
data = ['a', 'b', 'c', 'd', 'e']
selector = [True, False, 1, 0]
print(*compress(data, selector))
print(*zip(data, selector))
