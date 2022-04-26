
def factorials(n):
    result = 1
    for i in range(1, n+1):
        yield result
        result *= i


f = factorials(10)
print(f)
print(dir(f))
for i in f:
    print(i, end=', ')
print()
f = factorials(10)
print(list(f))
