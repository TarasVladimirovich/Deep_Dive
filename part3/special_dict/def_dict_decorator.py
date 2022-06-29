from collections import defaultdict, namedtuple
from datetime import datetime
from functools import wraps


def function_stats():
    d = defaultdict(lambda: {"count": 0,
                             "first_called": datetime.utcnow().strftime('%d/%m/%YT%H:%M:%S')})
    Stats = namedtuple('Stats', 'decorator data')

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            d[fn.__name__]['count'] += 1
            return fn(*args, **kwargs)

        return wrapper

    return Stats(decorator, d)


stats = function_stats()
print(stats.data)
# print(stats.decorator)


@stats.decorator
def func_1():
    pass


@stats.decorator
def func_2(x, y):
    pass


func_1()
func_1()
print(dict(stats.data))
func_2(10, 20)
print(dict(stats.data))