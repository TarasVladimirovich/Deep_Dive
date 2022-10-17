import collections

print(isinstance(0, collections.Hashable))
print(isinstance({1: 1}, collections.Hashable))
print(isinstance((1, 2), collections.Hashable))
print(isinstance((1, [1, 2, 3]), collections.Hashable))
v = ([], 2)
try:
    print(hash(v))
except TypeError as e:
    print(e)

q = [1, 2, 4]
b = [1, 2, 3, 4, 5]
print(q[len(q):])
print(b[len(q):])


def foo(q, v, s):
    for i in  vars().values():
        print(i)
    q = min(len(i) for i in vars().values())
    print('q', q)
    print(vars().keys())

foo([1, 2], [], [1, 2, 3])

print(None == None)
print(None is None)
# print(1 is int)
q = None
print(q is None)
print(q == None)
w = 'qwertyuqwertyuqwertyu'
s = 'qwertyuqwertyuqwertyu'
print(w is s)
print(w == s)
print(id(w), hex(id(s)))
q = (1, 2, 4)
print(q.count(1))