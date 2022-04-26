# print(help(map))
l1 = [1, 2, 3]
l2 = [10, 20, 30, 40]


def add(x, y):
    return x + y


print(list(map(add, l1, l2)))

