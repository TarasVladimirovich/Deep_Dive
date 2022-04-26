from dis import dis
from timeit import timeit
import sys

# print(dis(compile('(1, 2 ,3, "a")', 'string', 'eval')))
# print(dis(compile('[1, 2 ,3, "a"]', 'string', 'eval')))
# print(dis(compile('(1, 2 ,3, [1, 2])', 'string', 'eval')))

# print(timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=100_000_000))
# print(timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=100_000_000))

l1 = [1, 2, 5]
t1 = (1, 2, 5)
l2 = list(l1)
t2 = tuple(t1)
print(id(l1), id(l2), 'Different')
print(id(t1), id(t2), f'The same: {id(t1) == id(t2)}')

# Storage Efficiency
t = tuple()
prev = sys.getsizeof(t)
for i in range(10):
    c = tuple(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i +1} items: {size_c}, delta={delta}, c={c}')

l = list()
prev = sys.getsizeof(l)
for i in range(10):
    c = list(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i +1} items: {size_c}, delta={delta}, c={c}')

qw = list()
prev = sys.getsizeof(qw)
print(f'0 items: {prev}')
for i in range(10):
    c.append(i)
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i +1} items: {size_c}, delta={delta}, c={c}')