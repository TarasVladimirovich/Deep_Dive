from contextlib import contextmanager
from time import perf_counter, sleep


@contextmanager
def timer():
    stats = dict()
    stats['start'] = perf_counter()
    try:
        yield stats
    finally:
        stats['end'] = perf_counter()
        stats['elapsed'] = stats['end'] - stats['start']


with timer() as stats:
    sleep(1)

print(stats)
