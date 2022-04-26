from collections import namedtuple, Counter, defaultdict
from datetime import datetime
from functools import partial

file_ = 'nyc_parking_tickets_extract.csv'
with open(file_) as f:
    column_header = next(f).strip('\n').split(',')

column_names = [header.replace(' ', '_').lower() for header in column_header]
Ticket = namedtuple('Ticket', column_names)


def read_data():
    with open(file_) as f:
        next(f)
        yield from f


def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, *, default=None):
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default


def parse_str(value, *, default=None):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        return cleaned
    except ValueError:
        return default


column_parser = (parse_int,
                 parse_str,
                 lambda x: parse_str(x, default=''),  # the same as partial
                 partial(parse_str, default=''),  # the same as lambda
                 parse_date,
                 parse_int,
                 partial(parse_str, default=''),
                 parse_str,
                 partial(parse_str, default=''),
                 )


def parse_row(row, *, default=None):
    fields = row.strip('\n').split(',')
    parsed_data = [func(field) for func, field in zip(column_parser, fields)]
    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    else:
        return default


# generator function
def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed


# for row in read_data():
#     parsed_row = parse_row(row)
#     if parsed_row is None:
#         print(*zip(column_names, row.strip('\n').split(',')))

makes_count = {}
makes_count2 = defaultdict(int)

for data in parsed_data():
    if data.vehicle_make in makes_count:
        makes_count[data.vehicle_make] += 1
    else:
        makes_count[data.vehicle_make] = 1

for data in parsed_data():
    makes_count2[data.vehicle_make] += 1

print(Counter(data.vehicle_make for data in parsed_data()))
print(makes_count)
print(makes_count2)
print(*sorted(makes_count.items(),
              key=lambda x: x[1],
              reverse=True))
