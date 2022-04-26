l = ['a', 'q', 'A', 'ds', 'Q', 'q']
print(sorted(l))
print(sorted(l, key=lambda ch: ch.upper()))
d = {'q': 200, 'w': 100, 'e': 400, 'r': 300}
print(sorted(d, key=lambda x: d[x]))
print(dir(sorted))
print(sorted)
print(callable(5))

