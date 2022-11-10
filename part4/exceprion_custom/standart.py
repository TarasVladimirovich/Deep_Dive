print(type(Exception), type(BaseException))
ex = Exception()

print(ex.__class__, type(ex))
print(issubclass(IndexError, LookupError))
print(issubclass(LookupError, Exception))

l = [1, 2, 3]

try:
    l[4]
except IndexError as ex:
    print(ex.__class__, ':', ex)

try:
    l[4]
except LookupError as ex:
    print(ex.__class__, ':', str(ex))

try:
    l[4]
except Exception as ex:
    print(ex.__class__, ':', str(ex))

try:
    l[4]
except:
    print("Exception")

ex = ValueError('custom message')
print(str(ex), repr(ex))


def func_1():
    func_2()


def func_2():
    try:
        func_3()
    except ValueError:
        print('error occurred - silencing it')


def func_3():
    # create an instance of a ValueError exception, and raise it
    raise ValueError()


func_1()


def square(seq, index):
    return seq[index] ** 2


def squares(seq, max_n):
    for i in range(max_n):
        yield square(seq, i)


l = [1, 2, 3]
print(list(squares(l, 3)))


def square(seq, index):
    return seq[index] ** 2


def squares(seq, max_n):
    for i in range(max_n):
        try:
            yield square(seq, i)
        except Exception:
            return


l = [1, 2, 3]
list(squares(l, 5))
