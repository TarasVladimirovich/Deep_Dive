# |= &= -= ^=

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(id(s1), id(s2))
s1 = s1 & s2
print(f'{id(s1)=}, {id(s2)=} = Change id')
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(id(s1), id(s2))
s1 &= s2
print(f'{id(s1)=}, {id(s2)=} = Mutate s1 the same id')
