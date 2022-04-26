class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'Kyiv', 'Boryspil']
        self._index = 0

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        return CityIterator(self)

    def __getitem__(self, item):
        return self._cities[item]


class CityIterator:
    def __init__(self, city_obj: Cities):
        self._city_obj = city_obj
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._city_obj):
            raise StopIteration
        else:
            item = self._city_obj._cities[self._index]
            self._index += 1
            return item


cities = Cities()

for city in cities:
    print(city)

for city in cities:
    print(city)

print(next(cities))