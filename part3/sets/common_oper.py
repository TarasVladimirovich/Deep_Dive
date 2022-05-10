from sys import getsizeof
from timeit import timeit

s = {i for i in range(3)}
print(s)
print(f'{len(s):.3f}')
print(f'{len(s)=}')
print(f'{1 in s=}')
print(f'{11 in s=}')

n = 100_100
search = 99_999
number = 1000
l = [i for i in range(n)]
s = {i for i in range(n)}
d = {i: None for i in range(n)}

t_l = timeit(f'{search} in l', globals=globals(), number=number)
t_s = timeit(f'{search} in s', globals=globals(), number=number)
t_d = timeit(f'{search} in d', globals=globals(), number=number)
print(f'{t_l=}')
print(f'{t_s=}')
print(f'{t_d=}')
print(f'{getsizeof(l)=}')
print(f'{getsizeof(s)=}')
print(f'{getsizeof(d)=}')

s = {10, 20, 30}
s.add(1)
s.add(1)
print(s)
s.remove(10)
s.discard(10)  # Don't throw exception
# s.remove(10) Error
print(s)
s = set('python')
print(s.pop())  # remove random
print(s.pop())
print(s.pop())
print(s)
s.clear()
print(s)
