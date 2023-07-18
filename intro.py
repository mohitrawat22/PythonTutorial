# print a string
print("Hello World")

# print a number
print(5)

# print the computation
print(4*7)

# print more than one values
print("earth", 4)

# print format: print(value to print, sep(separator), end, file/place where we need to write the output, flush=flush)
# by default, end=\n and sep='', that is why after prnt next print is in new line and in multiple value print, each value has space in between
print("mohit", "rawat")
# below will print: mohit+++rawat---
# after this there will be no new line
print("mohit", "rawat", end="---", sep="+++")
print("Hello Mohit")


# comments

# single comment is by using #
'''
multi line comment
is by using
3 single or double quotes
'''


# escape sequences
# \n : print in new line
print("hello\nworld")

# \: if you want to use a special character as it is
print("Hello \"Mohit\"")


# variables and Data Types
# integer
a = 1
print(type(a))

# float
b = 1.2
print(type(b))

# string
c = "earth"
print(type(c))

# boolean
d = True
print(type(d))

# none
e = None
print(type(e))


# typecasting
a = "1"
b = "2"
print(a+b)
# explicit (converting string to int)
print(int(a)+int(b))
#implicit
c=2
d=2.3
# implicit (smaller data type is converted to higher data type by python)
print(c+d)

'''
# input from user
age = input("Enter your age ? ")
print(age)
# whatever you give as input, it will always be a STRING
print(type(age))
'''


# is vs ==
# is compares the memory location
# == compares the values
a = 4
b = "4"

# location is different
print(a is b)
# values are not same
print(a == b)

a = [1,2,3]
b = [1,2,3]
# python will create two lists
print(a is b)
# values of both lists are same
print(a == b)

a = 3
b = 3
# 3 is constant, so python will not create another 3
print(a is b)
# values are same
print(a == b)

a = "world"
b = "world"
# string is constant, so python will not create another string
print(a is b)
# values are same
print(a == b)

a = (1,2,3)
b = (1,2,3)
# tuple is constant, so python will not create another tuple
print(a is b)
# values are same
print(a == b)

a = None
b = None
# None is constant, so python will not create another None
print(a is b)
# values are same
print(a == b)
