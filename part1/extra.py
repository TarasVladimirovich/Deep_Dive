from collections import Counter, defaultdict

mylist = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 5, 6, 6]
c = Counter(mylist)
print(c)
print(c.most_common(), 'most_common')
print(c.most_common(2))
q = {}
print(q.get('t', 'qwerty'))
print(q.get('t'))

qw = defaultdict(int)
c = Counter(mylist)
for i in mylist:
    qw[i] += 1

print(qw)
print(c)