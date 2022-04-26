from time import perf_counter
from functools import wraps


def timed(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        print(f'spent {duration:.6f}s to run with {fn.__name__}')
        return result

    return wrapper


@timed
def mul(a, b):
    q = a ** b
    return 'Yes!'


@timed
def fib_rec(n):
    return calc_recursive_fib(n)


def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n - 1) + calc_recursive_fib(n - 2)


@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n + 1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2


print(fib_loop(35))
print(fib_rec(35))
