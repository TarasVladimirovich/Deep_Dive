# class Person:
#     pass
#
#
# try:
#     raise Person()
# except TypeError as ex:
#     print(repr(ex))

ex = BaseException('a', 'b', 'c')


# print(ex.args)
# print(repr(ex), str(ex))
# ex = ValueError('a', 'b', 'c')
# print(ex.args)
# print(str(ex))
# print(repr(ex))

# try:
#     raise ValueError('some message here')
# except ValueError as ex:
#     print(repr(ex))


def div(a, b):
    try:
        return a // b
    except ZeroDivisionError as ex:
        print('logging zero division exception: ', type(ex).__name__, ex.args)
        raise


# div(1, 0)


class CustomError(Exception):
    """a custom exception"""


def my_func(a, b):
    try:
        return a // b
    except ZeroDivisionError as ex:
        print('logging...')
        raise CustomError(*ex.args)


# my_func(1, 0)


# try:
#     raise ValueError('level 1')
# except ValueError:
#     try:
#         raise TypeError('level 2')
#     except TypeError:
#         raise KeyError('level 3')


class ConversionError(Exception):
    pass


def convert_int(val):
    if not isinstance(val, int):  # remember this will work for booleans too!
        raise TypeError()
    if val not in {0, 1}:
        raise ValueError("Integer values 0 or 1 only")
    return bool(val)


def convert_str(val):
    if not isinstance(val, str):
        raise TypeError()

    val = val.casefold()  # for case-insensitive comparisons
    if val in {'0', 'f', 'false'}:
        return False
    elif val in {'1', 't', 'true'}:
        return True
    else:
        raise ValueError('Admissible string values are: T, F, True, False (case insensitive)')


def make_bool(val):
    try:
        try:
            b = convert_int(val)
        except TypeError:
            # it wasn't an int/bool, so let's try it as a string
            try:
                b = convert_str(val)
            except TypeError:
                raise ConversionError(f'The type {type(val).__name__} cannot be converted to a bool') from None
    except ValueError as ex:
        # this will catch ValueError exceptions from either convert_int or convert_str
        raise ConversionError(f'The value {val} cannot be converted to a bool: {ex}') from None
    else:
        return b


# make_bool('ABC')


try:
    raise ValueError('level 1')
except ValueError as ex_1:
    try:
        raise ValueError('level 2')
    except ValueError as ex_2:
        try:
            raise ValueError('level 3')
        except ValueError as ex_3:
            raise ValueError('value error occurred') from ex_1

