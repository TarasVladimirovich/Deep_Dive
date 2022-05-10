s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
# intersections
print('intersections')
print(s1.intersection(s2))
print(s1.intersection(s2, s3))
print(s1 & s2)
print(s1 & s2 & s3)
print({1, 2}.intersection([2, 3]))
# print({1, 2} & [2, 3]) TypeError
# Union
print('Union')
print(s1.union(s2))
print(s1.union(s2, s3))
print(s1 | s2)
print(s1 | s2 | s3)
# isdisjoint
print(" isdisjoint Return True if two sets have a null intersection")
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {30, 40, 50}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))
if len(s1 & s2) > 0:
    print('not disjoint')

if s1 & s2:
    print('sets not disjoint')

if s1 & s3:
    print('sets not disjoint')
else:
    print((s1 & s3), bool(s1 & s3))
    print('sets disjoint')
# difference
print('difference')
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}
print(f'{s1 - s2=}')
print(f'{s1.difference(s2)=}')
print(f'{s2 - s1=}')
# symmetric_difference
print('symmetric_difference')
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
print(s2 ^ s1)
# subset superset
print('subset superset')
s1 = {1, 2, 3}
s2 = {1, 2, 3}
s3 = {1, 2, 3, 4}
s4 = {10, 20, 30}
print(f'{s1 is s2 = }')
print(f'{s1 == s2 = }')
print(f'{s1.issubset(s2) = }')
print(f'{s1 <= s2 = }')
print(f'{s1 < s2 = }')
print(f'{s1 < s3 = }')
print(f'{s3.issuperset(s2) = }')
print(f'{s3 > s2 = }')
print(f'{s3 >= s2 = }')
print(f'{s2 > s1 = }')

