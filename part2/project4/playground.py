import constants
import parse_utils

# for fname, cls_name, parser in zip(constants.fnames,
#                                    constants.class_names,
#                                    constants.parsers):
#     file_iter = parse_utils.iter_file(fname,
#                                       cls_name,
#                                       parser)
#     print(fname)
#     for _ in range(3):
#         print(next(file_iter))
#     print()
#
#
# gen = parse_utils.iter_combined_plain_tuple(constants.fnames,
#                                             constants.class_names,
#                                             constants.parsers,
#                                             constants.compress_fields)
# print(*next(gen))
# print(*next(gen))


header = [parse_utils.extract_field_names(fname) for fname in constants.fnames]
print(header)

# data_iter = parse_utils.iter_combined(constants.fnames,
#                                       constants.class_names,
#                                       constants.parsers,
#                                       constants.compress_fields)
# for row in itertools.islice(data_iter, 5):
#     print(row)
# data = parse_utils.iter_combined(constants.fnames,
#                                  constants.class_names,
#                                  constants.parsers,
#                                  constants.compress_fields)
#
#
# def group_key(item):
#     return item.gender, item.vehicle_make
#
#
# sorted_data = sorted(data, key=group_key)
# for row in itertools.islice(sorted_data, 3):
#     print(row)
#
# group_1 = itertools.groupby(sorted_data, key=group_key)
# group_2 = itertools.groupby(sorted_data, key=group_key)
#
# group_f = (item for item in group_1 if item[0][0] == 'Female')
# group_m = (item for item in group_2 if item[0][0] == 'Male')
# group_ff = ((item[0][1], len(tuple(item[1]))) for item in group_f)
# group_mm = ((item[0][1], len(tuple(item[1]))) for item in group_m)
#
# for row in group_ff:
#     print(row)
# print('*'*100)
# for row in group_mm:
#     print(row)


# data = parse_utils.iter_combined(constants.fnames,
#                                  constants.class_names,
#                                  constants.parsers,
#                                  constants.compress_fields)
# data1, data2 = itertools.tee(data, 2)
# def group_key(item):
#     return item.vehicle_make
# data_m = filter(lambda i: i.gender == 'Male', data1)  # (row for row in data if row.gender == 'Male)
# data_f = filter(lambda i: i.gender == 'Female', data2)  # (row for row in data if row.gender == 'Male)
# sorted_data_m = sorted(data_m, key=group_key)
# sorted_data_f = sorted(data_f, key=group_key)
# groups_m = itertools.groupby(sorted_data_m, key=group_key)
# groups_f = itertools.groupby(sorted_data_f, key=group_key)
# group_mm = ((item[0], len(tuple(item[1]))) for item in groups_m)
# group_ff = ((item[0], len(tuple(item[1]))) for item in groups_f)
# for row in group_mm:
#     print(row)
# print('-'*100)
# print('\n\n\n\n\n')
# for row in group_ff:
#     print(row)

# def group_key(item):
#     return item.vehicle_make
#
#
# def filtered_key(cutoff_date, gender, row):
#     return row.last_updated >= cutoff_date and row.gender == gender
#
#
# cutoff_date = datetime(2017, 3, 1)
#
# results_f = parse_utils.group_data(constants.fnames,
#                                    constants.class_names,
#                                    constants.parsers,
#                                    constants.compress_fields,
#                                    filter_key=partial(filtered_key, cutoff_date, 'Male'),
#                                    # filter_key=lambda row: filtered_key(cutoff_date, 'Male', row)
#                                    group_key=group_key
#                                    )
#
# for row in results_f:
#     print(row)

q = parse_utils.iter_file(constants.fname_personal, constants.personal_class_name, constants.personal_parser)
for i in q:
    print(id(i))
