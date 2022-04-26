class FactIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            import math
            result = math.factorial(self.i)
            self.i += 1
            return result


f = FactIter(10)
for n, i in enumerate(f):
    print(f'fact of {n}={i}')