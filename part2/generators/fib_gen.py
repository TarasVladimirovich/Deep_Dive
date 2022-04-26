from timeit import timeit
from functools import lru_cache


# recursive
# Fib(n) = Fib(n-1) + Fib(n-2)

class FibIter:

    def __init__(self, n):
        self.n = n
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= self.n:
            raise StopIteration
        else:
            result = self.fib(self._i)
            self._i += 1
            return result

    def fib(self, n):
        fib_0, fib_1 = 1, 1
        for i in range(n - 1):
            fib_0, fib_1 = fib_1, fib_0 + fib_1
        return fib_1


def fib_recursive(n):
    if n <= 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


@lru_cache()
def fib_recursive_cahced(n):
    if n <= 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_loop(n):
    fib_0, fib_1 = 1, 1
    for i in range(n - 1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1


def fib_gen(n):
    fib_0, fib_1 = 1, 1
    yield fib_0
    yield fib_1
    for i in range(n - 2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1


print('Recursive =', [fib_recursive(i) for i in range(7)])
print('Loop =', [fib_loop(i) for i in range(10)])
print('FibIter =', [i for i in FibIter(10)])
print('Generator =', [i for i in fib_gen(10)])
print(timeit('fib_recursive(10)', globals=globals(), number=10))
print(timeit('fib_recursive_cahced(10)', globals=globals(), number=10))
print(timeit('fib_loop(5000)', globals=globals(), number=10))
print(timeit('list(FibIter(5000))', globals=globals(), number=1))
print(timeit('list(fib_gen(5000))', globals=globals(), number=1))
