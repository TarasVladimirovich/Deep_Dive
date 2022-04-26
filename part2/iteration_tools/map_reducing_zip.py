from itertools import starmap, zip_longest
from functools import reduce

q = [(1, 1), (2, 3), range(3, 5)]


def add(x, y):
    return x + y


print(list(starmap(add, q)))

q = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(q)

q = reduce(lambda x, y: x * y, [1, 2, 3, 4], 10)
print(q)


def sum_(iterable):
    it = iter(iterable)
    res = next(it)
    yield res
    for i in it:
        res += i
        yield res


print(*sum_([10, 20, 3]))

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4]
l3 = [1, 2, 3]
print(*zip(l1, l2, l3))
print(*zip_longest(l1, l2, l3))
print(*zip_longest(l1, l2, l3, fillvalue=34))
print(help(zip_longest()))