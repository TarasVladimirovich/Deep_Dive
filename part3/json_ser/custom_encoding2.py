import json
from datetime import datetime
from typing import Any

default_encoder = json.JSONEncoder()


# print(default_encoder.encode([1, 2, 4]))


# class CustomJSONEncoder(json.JSONEncoder):
#     def default(self, o: Any) -> Any:
#         if isinstance(o, datetime):
#             return o.isoformat()
#         else:
#             super().default(o)

class CustomJSONEncoder(json.JSONEncoder):

    def __init__(self, *args, **kwargs):
        super().__init__(skipkeys=True,
                         allow_nan=False,
                         indent='--',
                         separators=('', ' = '))

    def default(self, o: Any) -> Any:
        if isinstance(o, datetime):
            return o.isoformat()
        else:
            super().default(o)


c_e = CustomJSONEncoder()
print(c_e.encode([1, 2, 4]))
print(c_e.encode(datetime.utcnow()))

print(json.dumps(dict(name='test', time=datetime.utcnow()),
                 cls=CustomJSONEncoder))
