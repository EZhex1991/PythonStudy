counter = 100
miles = 1000.0
name = "runoob"
print(counter, miles, name, sep='\t')

a = b = c = 1
print(a, b, c)
a, b, c, d, e = 1, 2.0, False, "runoob", 1 + 1j
print(a, b, c, d, e)
print(type(a), type(b), type(c), type(d), type(e))
print(isinstance(c, bool))


class A:
    pass


class B(A):
    pass


print(isinstance(B(), A), type(B()) == A)

print(2 + 10)
print(2 - 10)
print(2 * 10)
print(2 / 10)
print(2 // 10)
print(2 ** 10)
print(2 % 10)

str = "012345678"
print(str)
print(str[0])
print(str[1:4])
print(str[4:-2])
print(str[-2:])
print(str * 2)
print(str + "9")

str = "newli\ne"
print(str)
str = r"newli\ne"
print(str)

list = ['0', 1, True, 3.0, False, 5 + 1j]
print(list)
print(list[0])
print(list[1:3])
print(list[3:])
print(list * 2)
print(list + list[0:2])

list[2] = 2
print(list)
list[2:4] = ['2', '3']
print(list)
list[1:4] = ['1', '2']
print(list)

tuple = ('0', '1', 2, 3, 4.0)
print(tuple)

set1 = {'0', '1', '2', '0'}
set2 = {'2', '3'}
print(set1)

if ('3' in set1):
    print("'3' in set1")
else:
    print("'3' not in set1")

print(set1 | set2)
print(set1 - set2)
print(set1 & set2)
print(set1 ^ set2)

dict = {}
dict['1'] = '1'
dict[2] = 2
print(dict)
print('1', dict['1'])
print(2, dict[2])
print(dict.keys())
