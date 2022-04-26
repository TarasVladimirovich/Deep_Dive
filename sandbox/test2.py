import string

q = {i: ord(i) for i in string.ascii_lowercase}
print(q)

print(q.get('a'))
print(q.get('A', 'takkoe'))

qw = 'qwerty'

for i in enumerate(qw):
    print(i)
