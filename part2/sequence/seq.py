from collections import Counter

list_ = [1, 1, 1, 2, 2, 3, 4, 5, 6, 7, 5, 'c', 3, 3, 1]
q = Counter(list_)
w = dict(q)
print(w)
print(sorted(w, key=w.get))
print(2 * list_)
print(list_.index('c'))
try:
    print(hash((1, 2, [])))
except TypeError as errno:
    print(errno)
# The Different
qw = ['Taras', 'Ira']
print(id(qw))
qw = ['Taras', 'Ira'] + ['Kochan']
# The same
print(id(qw))
qw.append('Mac')
print(id(qw))


