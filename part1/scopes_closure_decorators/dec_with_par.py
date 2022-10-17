def outer(reps):

    from time import perf_counter
    from functools import wraps

    def timed(fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            print(f'spent {total_elapsed:.6f}s to run with {fn.__name__}')
            return result
        return inner

    return timed


@outer(10)
def q(a, b):
    return a ** b

q(1000, 1000)
