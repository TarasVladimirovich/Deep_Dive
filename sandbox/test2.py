# import string
#
# q = {i: ord(i) for i in string.ascii_lowercase}
# print(q)
#
# print(q.get('a'))
# print(q.get('A', 'takkoe'))
#
# qw = 'qwerty'
#
# for i in enumerate(qw):
#     print(i)

# q = filter(lambda x: 'a' in x, ['a', 'b', 'a', 'v'])
# assert filter(lambda x: 'aqw' in x, ['a', 'b', 'a', 'v'])
# assert [1]

# print(list(q))


q = (i for i in range(3))
items = []
items.append(q)
print(items)