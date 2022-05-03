from contextlib import contextmanager


@contextmanager
def open_file(fname):
    print(f'Opening file {fname}')
    f = open(fname)
    try:
        yield f
    finally:
        print('Closing file {fname}')
        f.close()


f_names = 'file1.txt', 'file2.txt', 'file3.txt'

enters = []
exits = []

for f_name in f_names:
    ctx = open_file(f_name)
    enters.append(ctx.__enter__)
    exits.append(ctx.__exit__)

files = [enter() for enter in enters]

while True:
    try:
        rows = [next(f).strip('\n') for f in files]
    except StopIteration:
        break
    else:
        row = ','.join(rows)
        print(row)

for fn in exits[::-1]:
    fn(None, None, None)


# ++++++++++++++++++++++

class NestedCtx:
    def __init__(self, *ctxs):
        self._enters = []
        self._exits = []
        self._values = []

        for ctx in ctxs:
            self._enters.append(ctx.__enter__)
            self._exits.append(ctx.__exit__)

    def __enter__(self):
        for enter in self._enters:
            self._values.append(enter())
        return self._values

    def __exit__(self, exc_type, exc_val, exc_tb):
        for exit in self._exits[::-1]:
            exit(exc_type, exc_val, exc_tb)
        return False


print('*' * 100)
with NestedCtx(open_file('file1.txt'),
               open_file('file2.txt'),
               open_file('file3.txt')) as files:
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ', '.join(rows)
            print(row)

# ++++++++++++++++++++++
print('*' * 100)


@contextmanager
def open_file(fname):
    print(f'Opening file {fname}')
    f = open(fname)
    try:
        yield f
    finally:
        print('Closing file {fname}')
        f.close()


class NestedCtx:
    def __init__(self):
        self._exits = []

    def __enter__(self):
        return self

    def enter_ctx(self, ctx):
        self._exits.append(ctx.__exit__)
        value = ctx.__enter__()
        return value

    def __exit__(self, exc_type, exc_val, exc_tb):
        for exit in self._exits[::-1]:
            exit(exc_type, exc_val, exc_tb)
        return False


with NestedCtx() as stack:
    files = [stack.enter_ctx(open_file(f)) for f in f_names]
    while True:
        try:
            rows = [next(f).strip('\n') for f in files]
        except StopIteration:
            break
        else:
            row = ', '.join(rows)
            print(row)
