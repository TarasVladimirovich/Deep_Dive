class RepeatIterable:
    def __init__(self, **kwargs):
        self.d = kwargs

    def __setitem__(self, key, value):
        self.d[key] = value

    def __getitem__(self, key):
        self.d[key] = self.d.get(key, 0)
        return self.d[key]

    def elements(self):
        for k, frequency in self.d.items():
            for i in range(frequency):
                yield k

r = RepeatIterable(a=2, b=3, c=1)

r['d'] = 4

for e in r.elements():
    print(e, end=', ')

print()

import random
from collections import Counter
from itertools import repeat, chain
random.seed(0)

widgets = ['battery', 'charger', 'cable', 'case', 'keyboard', 'mouse']

orders = [(random.choice(widgets), random.randint(1, 5)) for _ in range(100)]
refunds = [(random.choice(widgets), random.randint(1, 3)) for _ in range(20)]

print(orders)
print(refunds)

sold_counter = Counter()
refund_counter = Counter()

for order in orders:
    sold_counter[order[0]] += order[1]

for refund in refunds:
    refund_counter[refund[0]] += refund[1]

print(sold_counter)
print(refund_counter)
net_counter = sold_counter - refund_counter
print(net_counter)

# print(list(repeat(*orders[0])))
#
# print(list(chain.from_iterable(repeat(*order) for order in orders)))
order_counter = Counter(chain.from_iterable(repeat(*order) for order in orders))
print(order_counter)