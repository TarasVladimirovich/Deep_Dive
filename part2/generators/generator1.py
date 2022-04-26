def my_func():
    yield 1
    yield 2
    yield 3


# generators are iterators
# they implemented the iterator protocol

gen = my_func()
print(next(gen))
print(next(gen))
p = iter(gen)
print(next(p))


class Squares:

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return Squares.squares_gen(self.n)

    @staticmethod
    def squares_gen(n):
        for i in range(n):
            yield i ** 2


sq = Squares(10)
print(list(sq))
print(list(sq))
