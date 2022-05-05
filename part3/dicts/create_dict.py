import string

q = {'key': 'value'}
w = dict(key='value', q='w')

e = dict.fromkeys([1, 2, 4])
print(e)
e = dict.fromkeys([1, 2, 4], 'N/A')
print(e)

print(dict(zip('abc', range(1, 4))))

text = 'sdfgnbgfdvcfb fgh  ggbvf fgnd  fgn fg ghbfzbgfdf`zzgFgmlkdjznmloidug`fD'
counts = {}
for c in text:
    counts[c] = counts.get(c, 0) + 1

print(counts)


