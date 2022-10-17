# d = {'a': 1, 'b': 2, 'c': 3}
# d['b'] = 100
# print(d)
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# d3 = {'a': 1, 'b': 4}
# print(d1.update(d2))
# print(d1)
# d1.update(d3)
# print(d1)
d1 = {'a': 1, 'b': 2}
d1.update(b=20, c=30, g=40)
print(d1)
# d1 = {'a': 1, 'b': 2}
# d1.update((['b', 20], ['c', 30], ('g', 40), {'qwe', 33}))
# print(d1)
# d1 = {'a': 1, 'b': 2}
# d1.update(((k, ord(k)) for k in 'python'))
# print(d1)
# print(dict(((k, ord(k)) for k in 'python')))
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# print(dict(**d1, **d2))
#
# conf = dict.fromkeys(('a', 'b', 'c', 'd'), None)
# print(conf)
