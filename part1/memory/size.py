q = [i for i in range(1000)]
w = (i for i in range(1000))
e = ([i for i in range(1000)])

print(q.__sizeof__())
print(w.__sizeof__())
print(e.__sizeof__())