import csv
from collections import namedtuple
from itertools import islice

f_names = 'cars.csv', 'personal_info.csv'

for f_name in f_names:
    with open(f_name) as f:
        print(next(f), end='')
        print(next(f), end='')
    print(f'\n{"*" * 100}')


# with open(f_names[0]) as f:
#     dialect = csv.Sniffer().sniff(f.read(1000))
#
# print(dialect.delimiter)
# print(vars(dialect))


def get_dialect(f_name):
    with open(f_name) as f:
        return csv.Sniffer().sniff(f.read(1000))


class FileParsed:
    def __init__(self, f_name):
        self.f_name = f_name

    def __enter__(self):
        self._f = open(self.f_name, 'r')
        self._reader = csv.reader(self._f, get_dialect(self.f_name))
        headers = map(str.lower, next(self._reader))
        self._nt = namedtuple('Data', headers)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._f.close()
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self._f.closed:
            raise StopIteration
        else:
            return self._nt(*next(self._reader))


with FileParsed('cars.csv') as data:
    for row in islice(data, 1):
        print(row)
