l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(id(l1), id(l2))
l1 = l1 + l2

print(id(l1), id(l2), 'change l1 id')

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(id(l1), id(l2))
l1 += l2
print(id(l1), id(l2), 'the same l1 id')


l1 = [1, 2, 3]
t1 = (4, 5, 6)
# l1 = l1 + t1 can't do it
l1 += t1
print(l1, 'concatenate list + tuple, list extended and id not changed')

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(id(t1), id(t2))
t1 = t1 + t2
print(id(t1), id(t2))
print(t1)
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(id(t1), id(t2))
t1 += t2
print(id(t1), id(t2))
print(t1)
