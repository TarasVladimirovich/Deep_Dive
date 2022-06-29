from collections import defaultdict

d = {}
d['a'] = d.get('a', 0) + 1
print(d)

counts = {}
sentence = 'able was I era I saw elba'
for c in sentence:
    counts[c] = counts.get(c, 0) + 1
print(counts)

counts = defaultdict(lambda: 0)  # defaultdict(int)
for c in sentence:
    counts[c] += 1
print(counts)
print(counts.items())
print(isinstance(counts, defaultdict))
print(isinstance(counts, dict))

persons = {
    'john': {'age': 20, 'eye_color': 'blue'},
    'jack': {'age': 25, 'eye_color': 'brown'},
    'jill': {'age': 22, 'eye_color': 'blue'},
    'eric': {'age': 35},
    'michael': {'age': 27}
}

eye_colors = defaultdict(list)
for person, details in persons.items():
    color = details.get('eye_color', 'Unknown')
    eye_colors[color].append(person)

print(eye_colors)