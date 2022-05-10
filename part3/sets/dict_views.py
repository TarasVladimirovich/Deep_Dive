d = {'a': 1, 'b': 10, 'v': 34}
key = d.keys()
value = d.values()
items = d.items()
print(key)
print(value)
print(items)
d['qwe'] = 666
print(key)
print(value)
print(items)
# Views - dynamic
# Error will be with all Views
# d = dict(zip('abc', '123'))
# for k, v in d.items():
#     print(k, v)
#     del d[k]
# RuntimeError: dictionary changed size during iteration

# d = dict(zip('abc', '123'))
# for k, v in d.items():
#     print(k, v)
#     d['z'] = 1000
# RuntimeError: dictionary changed size during iteration
