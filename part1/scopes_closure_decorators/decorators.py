# def counter(fn):
#     count = 0
#
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'fn {fn.__name__}, was calles {count} times')
#         return fn(*args, **kwargs)
#
#     inner.__name__ = fn.__name__
#     inner.__doc__ = fn.__doc__
#     return inner


from functools import wraps


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'fn {fn.__name__}, was calles {count} times')
        return fn(*args, **kwargs)

    # inner = wraps(fn)(inner())
    return inner


@counter
def mult(a, b, c):
    """
    Takkoe
    :param a:
    :param b:
    :param c:
    :return:
    """
    return a * b * c


print(mult.__name__)
