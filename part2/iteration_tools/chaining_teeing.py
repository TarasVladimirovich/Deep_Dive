from itertools import chain

l1 = (i ** 2 for i in range(4))
l2 = (i ** 2 for i in range(4, 8))
l3 = (i ** 2 for i in range(8, 12))

for gen in l1, l2, l3:
    for item in gen:
        print(item, end=' ')
print()

l1 = (i ** 2 for i in range(4))
l2 = (i ** 2 for i in range(4, 8))
l3 = (i ** 2 for i in range(8, 12))

for item in chain(l1, l2, l3):
    print(item, end=' ')
print()