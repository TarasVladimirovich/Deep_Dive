import csv
from datetime import datetime
from collections import namedtuple
from itertools import chain, compress, groupby


def csv_parser(fname, *, delimiter=',', quotechar='"', incluse_header=False):
    with open(fname) as f:
        reader = csv.reader(f,
                            delimiter=delimiter,
                            quotechar=quotechar)
        if not incluse_header:
            next(f)  # tha same as next(reader)
        yield from reader


def extract_field_names(fname):
    reder = csv_parser(fname, incluse_header=True)
    return next(reder)


def parse_date(value, *, fmt='%Y-%m-%dT%H:%M:%SZ'):
    return datetime.strptime(value, fmt)


def create_named_tuple_class(fname, class_name):
    fields = extract_field_names(fname)
    return namedtuple(class_name, fields)


def create_combo_named_tuple_class(fnames, compress_fields):
    compress_fields = chain.from_iterable(compress_fields)
    fields_names = \
        chain.from_iterable((extract_field_names(fname) for fname in fnames))
    compressed_fields_names = compress(fields_names, compress_fields)
    return namedtuple('Data', compressed_fields_names)


def iter_file(fname, class_name, parser):
    nt_class = create_named_tuple_class(fname, class_name)
    reader = csv_parser(fname)
    for row in reader:
        parsed_data = (parse_fn(value) for value, parse_fn in zip(row, parser))
        yield nt_class(*parsed_data)


def iter_combined_plain_tuple(fnames, class_names, parsers, compress_fields):
    compress_fields = tuple(chain.from_iterable(compress_fields))
    zipped_tuples = zip(*(iter_file(f, c, p)
                          for f, c, p in zip(fnames, class_names, parsers)))
    merged_iter = (chain.from_iterable(zipped_tuple)
                   for zipped_tuple in zipped_tuples)  # chain(*zipped_tuple)
    for row in merged_iter:
        compressed_row = compress(row, compress_fields)
        yield compressed_row


def iter_combined(fnames, class_names, parsers, compress_fields):
    combo_nt = create_combo_named_tuple_class(fnames, compress_fields)
    compress_fields = tuple(chain.from_iterable(compress_fields))
    zipped_tuples = zip(*(iter_file(f, c, p)
                          for f, c, p in zip(fnames, class_names, parsers)))
    merged_iter = (chain.from_iterable(zipped_tuple)
                   for zipped_tuple in zipped_tuples)  # chain(*zipped_tuple)
    for row in merged_iter:
        compressed_row = compress(row, compress_fields)
        yield combo_nt(*compressed_row)


def filtered_iter_combined(fnames, class_names, parsers, compress_fields, *, key=None):
    iter_combo = iter_combined(fnames,
                               class_names,
                               parsers,
                               compress_fields)

    yield from filter(key, iter_combo)


def group_data(fnames, class_names, parsers, compress_fields, filter_key, group_key):
    data = filtered_iter_combined(fnames,
                                  class_names,
                                  parsers,
                                  compress_fields,
                                  key=filter_key)

    # data_filtered = (row for row in data if row.gender == gender)  # filter(lambda i: i.gender == gender, data)
    sorted_data = sorted(data, key=group_key)
    groups = groupby(sorted_data, key=group_key)
    group_counts = ((g[0], len(tuple(g[1]))) for g in groups)
    return sorted(group_counts, key=lambda row: row[1], reverse=True)
