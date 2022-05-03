def respond(lan):
    match lan:
        case 'Java' | 'Javascript':
            return 'Java1'
        case 'pyt':
            return 'pyt1'
        case 'qwe':
            return 'Javrtya1'
        case _:
            return 'Takkoe'


# print(respond('Javascript'))
# print(respond('Java'))

symbols = {'F': 'f', 'B': 'b'}


def op(command):
    match command:
        case ['move', ('F' | 'B') as direction]:
            return symbols[direction]
        case 'pyt':
            return 'pyt1'
        case 'qwe':
            return 'Javrtya1'
        case _:
            return 'Takkoe'


print(op(['move', 'F']))

print(set('Q') <= symbols.keys())
print(set('FB') <= symbols.keys())
