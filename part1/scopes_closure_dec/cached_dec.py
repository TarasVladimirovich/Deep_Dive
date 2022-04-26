def memorize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


@memorize
def fib(n):
    print(f'Calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)


print(fib(10))
print(fib(9))
print(fib(11))

from functools import lru_cache

@lru_cache()
def fib(n):
    print(f'Calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(10))
print(fib(10))
print(fib(10))