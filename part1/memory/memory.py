import sys
import ctypes
# check id of memory
my_var = 10
print(id(my_var))
print(hex(id(my_var)))
print(type(my_var))

my_var1 = my_var
my_var2 = my_var
# return +1 count in this case
count = sys.getrefcount(my_var)
print(count)

a = [1, 2, 3]
print(sys.getrefcount(a))
# return ref count of var
print(ctypes.c_long.from_address(id(a)).value)
b = a
print(ctypes.c_long.from_address(id(b)).value)
print(ctypes.c_long.from_address(id(my_var)).value)

q = 'string'
print(id(q))
q = 1234
print(id(q))
print(id(q+150))

s = (1, 2, 3)
print(id(s))
print(dir(s))
