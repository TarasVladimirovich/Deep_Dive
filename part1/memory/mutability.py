t = (1, 2, 3)
a = [1, 2]
b = [3, 4]
c = (a, b)
# print(hash(c)) # Error, lists are mutable
print(hash(t))

print(id(a))
a = a + [10]
print(id(a))
print('dictionary')
my_dict = {'a': 1, 'b': 2}
print(id(my_dict))
my_dict['c'] = 3
# tha same
print(id(my_dict))


def process(lst):
    lst.append(100)


my_list = [1, 2, 3]
process(my_list)
print(my_list)
print('-'*100)
qw = 'hello'
qe = 'hello'
print(qw is qe)
print(qw == qe)

print(id(process(my_list)))
# print(help(dir()))
c1 = int('101', base=2)
print(c1)
