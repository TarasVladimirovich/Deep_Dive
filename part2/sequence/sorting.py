t = 1, 2, 4, 5, 6, 3, 2, 45, 232, 535, 1, 23, 343, 34

print(sorted(t))
print(t)
d = {3: 100, 2: 200, 1: 300}
print(d.items())
print(sorted(d))
print(sorted(d, key=d.get))
print(sorted(d, key=lambda k: d[k]))
print(sorted(d.items(), key=lambda item: item[1]))
print({k: v for k, v in sorted(d.items(), key=lambda item: item[1])})