class CyclicIterator:
    def __init__(self, lst, length):
        self.lst = lst
        self.i = 0
        self.length = length

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.lst[self.i % len(self.lst)]
            self.i += 1
            return result


iter_cucl = CyclicIterator('NSWE', 12)
for i in iter_cucl:
    # print(f'i={i} ', i % 4, end=' ')
    print(i, end=' ')

n = 23
print()
print([str(number) + direction for number, direction in zip(range(1, n + 1), 'NSWE' * (n // 4 + 1))])

import itertools


class CyclicIterator2:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.lst[self.i % len(self.lst)]
        self.i += 1
        return result


iter_cucl = CyclicIterator2('NSWE')
print([f'{i}{next((iter_cucl))}' for i in range(1, 11)])
iter_cucl = itertools.cycle('NSWE')
print([f'{i}{next((iter_cucl))}' for i in range(1, 11)])
print([f'{i}{next((iter_cucl))}' for i in range(1, 11)])
