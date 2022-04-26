# int range [-5, 256]
a = 10
b = 10
print(id(a), id(b))
a = 12345678900000000
b = 12345678900000000
print(id(a), id(b))
print(a is b)

import sys
q = sys.intern('q w e r t y')
c = sys.intern('q w e r t y')
# == compare chr by chr


q = {'123': 123}
print(q.get('qwe'))
print('123' in q)
