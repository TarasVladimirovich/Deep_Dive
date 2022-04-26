l = [1, 2, 3]
cp = [e for e in l]
cp1 = l[:]
cp2 = list(l)
print(id(l))
print(id(cp))
print(id(cp1))

sl = slice(14, 88)
print(sl)
print(type(sl))
print(l[sl])
print(sl.start)
print(sl.stop)

qw = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(list(enumerate(qw)))
print(qw[1])
print(qw[-1])
print(qw[3:7])
print(qw[-3:-1])
print(qw[-3:])
print(qw[::-1])
print(qw[::1])
print(qw[::2])
print(qw[2::2])
print(qw[::-2])
