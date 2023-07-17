# how import works

'''
import math
num1 = math.sqrt(9)
print(num1)


from math import sqrt
num1 = sqrt(9)
print(num1)


from math import *
num1 = sqrt(9)
print(num1)
'''

import math as m
num1 = m.sqrt(9)
print(num1)

# print all functions and variables inside a module
print(dir(m))

print()
import env1
env1.func1()
print(env1.num2)
env1.func2()


# local and global variables
x = 10
print(f'global: {x}')

def hello():
    x = 5
    print(f'local: {x}')

print(f'global: {x}')
hello()
print(f'global: {x}')

def hello1():
    global x
    x = 5
    print(f'local (now global): {x}')

print(f'global: {x}')
hello1()
print(f'global: {x}')
