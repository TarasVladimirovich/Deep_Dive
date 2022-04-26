# False
# None, False, 0 (any numeric), empry seq and mapping type
print(False == 0)
print(False == bool([]))
assert False == 0
assert False == bool([])
assert False == bool('')
assert False == bool(())
assert False == bool({})

q = [True, False]
print(any(q))
print('any ', any([0, '', None]))
print('any 2', any([0, '', None, (1, 2)]))
print(all(q))
print(all([True, True]))


# predicate = pred

def squares(n):
    return (i ** 2 for i in range(n))


print(min(squares(5)))
print(max(squares(6)))
print(sum(squares(5)))


def is_numeric(v):
    return isinstance(v, int)

l = [1, 2, 3, 4, 5]
l1 = [1, 2, 3, 4, 'a']
pred_l = map(is_numeric, l)
pred_l1 = map(lambda x: isinstance(x, int), l1)
print(all(pred_l))
print(all(pred_l1))