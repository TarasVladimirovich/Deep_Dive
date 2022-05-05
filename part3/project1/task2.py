d1 = dict(zip('abcd', range(1, 5)))
d2 = dict(zip('bcyz', range(20, 60, 10)))


def intersect(d1, d2):
    d1_keys = d1.keys()
    d2_keys = d2.keys()
    keys = d1_keys & d2_keys
    return {k: (d1[k], d2[k]) for k in keys}


print(intersect(d1, d2))
