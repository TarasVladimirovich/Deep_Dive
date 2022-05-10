from data import template, john, eric, michael, iryna


def match_key(data: dict, validator: dict, path: str):
    data_keys = data.keys()
    valid_keys = validator.keys()

    extra_keys = data_keys - valid_keys
    missing_keys = valid_keys - data_keys

    if missing_keys or extra_keys:
        missing_msg = ('missing keys: ' +
                       ', '.join({path + '.' + str(key)
                                  for key in missing_keys})) \
            if missing_keys else ''

        extra_msg = ('extra keys: ' +
                     ', '.join({path + '.' + str(key)
                                for key in extra_keys})) \
            if extra_keys else ''
        raise SchemaKeyMismatch(' '.join((missing_msg, extra_msg)))


def match_type(data: dict, validator: dict, path: str):
    for key, value in validator.items():
        if isinstance(value, dict):
            valid_type = dict
        else:
            valid_type = value
        data_value = data.get(key, object())
        if not isinstance(data_value, valid_type):
            err_msg = ('incorrect type: ' + path + '.' + key + ' -> expected '
                       + valid_type.__name__ + ', found ' + type(data_value).__name__)
            raise SchemaTypeMismatch(err_msg)


def recurse_validate(data: dict, validator: dict, path: str):
    match_key(data, validator, path)
    match_type(data, validator, path)

    dict_type_key = {key for key, value in validator.items()
                     if isinstance(value, dict)}

    for key in dict_type_key:
        sub_path = path + '.' + str(key)
        sub_validator = validator[key]
        sub_data = data[key]
        recurse_validate(sub_data, sub_validator, sub_path)


class SchemaError(Exception):
    pass


class SchemaKeyMismatch(SchemaError):
    pass


class SchemaTypeMismatch(SchemaError, TypeError):
    pass


def validate(data, validator):
    recurse_validate(data, validator, '')


validate(john, template)
try:
    validate(iryna, template)
except SchemaError as e:
    print(e)

try:
    validate(michael, template)
except SchemaError as e:
    print(e)
try:
    validate(eric, template)
except SchemaError as e:
    print(e)
