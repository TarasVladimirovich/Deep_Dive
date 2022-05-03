from time import perf_counter, sleep


class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.star = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.star
        return False


with Timer() as timer:
    sleep(1)

print(timer.elapsed)
