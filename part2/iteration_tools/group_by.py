from itertools import groupby

data = (1, 2, 2, 2, 2, 3, 3, 5)
print(list(groupby(data)))
it = groupby(data)
for group_key, sub_iter in it:
    print(group_key, list(sub_iter))

data = (
    (1, 'abc'),
    (1, 'abc'),
    (1, 'bcd'),

    (2, 'qwe'),
    (2, 'rty'),

    (3, 'asd'),
)

groups = groupby(data, key=lambda x: x[0])
print(groups)
for group_key, sub_iter in groups:
    print(group_key, list(sub_iter))