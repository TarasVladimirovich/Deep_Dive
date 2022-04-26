# ліст [1,0 [1,0,[1, 0]], [1,0]]

q = [1, 0, [1, 0, [1, 0]], [1, 0]]


# list, int
def foo(o: list, n, sum_=0):  # порахувати кількість листів і  фбо чисел 1
    for i in o:
        if i == n:
            sum_ += 1
        if isinstance(i, list):
            sum_ = foo(i, n, sum_)
    return sum_


print(foo(q, ))
