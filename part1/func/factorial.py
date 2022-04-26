def fac(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print(f'calc {n}!')
        result = n * fac(n-1)
        cache[n] = result
        return result
