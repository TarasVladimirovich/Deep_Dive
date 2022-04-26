a = 10
b = 11
print(a, b)
a, b = b, a
print(a, b)
l = [1, 2, 3, 4, 5]
a, *b = l
print(a)
print(b)

a, *b = (1, 2, 3, 4, 5)
print(a)
print(b) # unpackig into list

a, *b, c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print([*l1, *l2])
