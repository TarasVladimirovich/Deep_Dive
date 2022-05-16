from json import loads, dumps, JSONDecodeError

from jsonschema import validate
from jsonschema import ValidationError

person_schema = {
    "type": "object",
    "properties": {
        "firstName": {
            "type": "string",
            "minLength": 1
        },
        "middleInitial": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1
        },
        "lastName": {
            "type": "string",
            "minLength": 1
        },
        "age": {
            "type": "integer",
            "minimum": 0
        },
        "eyeColor": {
            "type": "string",
            "enum": ["amber", "blue", "brown", "gray",
                     "green", "hazel", "red", "violet"]
        }
    },
    "required": ["firstName", "lastName"]
}

p1 = '''
    {
        "firstName": "John",
        "middleInitial": "M",
        "lastName": "Cleese",
        "age": 79
    }
'''

p2 = '''
    {
        "firstName": "John",
        "middleInitial": 100,
        "lastName": "Cleese",
        "age": "Unknown"
    }
'''

p3 = '''
    {
        "firstName": "John",
        "age": -10.5
    }
'''

p4 = '''
    {
        "firstName": "John",
        "middleInitial": null,
        "lastName": "Cleese",
        "eyeColor": "blue-gray"
    }
'''

# print(p1)

try:
    validate(loads(p1), person_schema)
except JSONDecodeError as ex:
    print(f'Invalid JSON: {ex}')
except ValidationError as ex:
    print(f'Validation error: {ex}')
else:
    print('JSON is valid')


from jsonschema import Draft4Validator

validator = Draft4Validator(person_schema)

for error in validator.iter_errors(loads(p4)):
    print(error, end='\n-----------\n')