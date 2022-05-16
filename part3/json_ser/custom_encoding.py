from datetime import datetime
from functools import singledispatch
import json

current = datetime.utcnow()


def format_iso(dt):
    format = '%Y-%m-dT%H:%M:%S'
    return dt.strftime(format)


log_ = {'time': datetime.utcnow(), 'message': 'testing'}
# print(json.dumps(log_, indent=2))
print(json.dumps(log_, indent=2, default=format_iso))


def format_iso(arg):
    return 'Unknown ser'


print(json.dumps(log_, indent=2, default=format_iso))


@singledispatch
def json_format(arg):
        print(arg)
        try:
            print('\ttry tojson')
            return arg.toJSON()
        except AttributeError:
            try:
                print('\ttry vars')
                return vars(arg)
            except TypeError:
                print('\ttry repr')
                return str(arg)


@json_format.register(datetime)
def _(arg):
    return arg.isoformat()


@json_format.register(set)
def _(arg):
    return list(arg)

print('*'*100)
print(json.dumps(log_, default=json_format, indent=2))
