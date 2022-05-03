def open_file(fname, mode='r'):
    print('Opening file....')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('Closing file....')
        f.close()


class GenContextManager:
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        print('Calling next to yielded')
        return next(self.gen)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Calling next to perform')
        try:
            next(self.gen)
        except StopIteration:
            pass
        return False


file_gen = open_file('test.txt')
with GenContextManager(file_gen) as f:
    print(f.readlines())


def context_manager_dec(gen_fn):
    def helper(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        ctx = GenContextManager(gen)
        return ctx

    return helper


@context_manager_dec
def open_file(fname, mode='r'):
    print('Opening file....')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('Closing file....')
        f.close()


# file_gen = context_manager_dec(open_file)
print()
with open_file('test.txt') as f:
    print(f.readlines())

from contextlib import contextmanager


@contextmanager
def open_file(fname, mode='r'):
    print('Opening file....')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('Closing file....')
        f.close()


print()
with open_file('test.txt') as f:
    print(f.readlines())
