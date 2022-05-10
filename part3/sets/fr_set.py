from functools import lru_cache


@lru_cache()
def foo(*, a, b):
    print(f'calculating {a=} {b=}')
    return f'result {a+b = }'


print(foo(a=1, b=2))
print(foo(a=1, b=2))
print(foo(a=1, b=2))
print(foo(a=2, b=1))
print(foo(a=2, b=1))
print(foo(a=1, b=2))


# print(foo(a=[1], b=[2])) TypeError: unhashable type: 'list'


def memoizer(fn):
    cache = {}

    def inner(*args, **kwargs):
        key = (*args, frozenset(kwargs.items()))
        if key not in cache:
            result = fn(*args, **kwargs)
            cache[key] = result
        return cache[key]

    return inner


@memoizer
def foo2(*, a, b):
    print(f'calculating {a=} {b=}')
    return f'result {a+b = }'


print('*' * 100)
print(foo2(a=1, b=2))
print(foo2(a=1, b=2))
print(foo2(a=1, b=2))
print(foo2(b=2, a=1))
print(foo2(a=2, b=1))
print(foo2(b=1, a=2))


def memoizer(fn):
    cache = {}

    def inner(*args, **kwargs):
        key = frozenset(args) | frozenset(kwargs.items())
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
            return cache[key]

    return inner


@memoizer
def adder(*args):
    print(f'calculating {[*args]}')
    return sum(args)


print(adder(1, 2, 3))
print(adder(2, 3, 1))
