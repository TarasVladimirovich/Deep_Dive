composers = {'Johann': 65,
             'Ludwig': 56,
             'Frederic': 39,
             'Wolfgang': 35
             }

print(sorted(composers.items(), key=lambda x: x[1], reverse=True))
print(sorted(composers, key=composers.get, reverse=True))
