def matrix(n):
    gen = (
        (i * j for j in range(1, n + 1))
        for i in range(1, n + 1)
    )
    return gen


m = list(matrix(5))


def matrix_iter(n):
    for row in matrix(n):
        yield from row


m = list(matrix_iter(5))
print(m)
