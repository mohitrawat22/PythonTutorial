'''
list1 = [1,2,3]

# all attributes and methods available for an object
print(dir(list1))
print(list1.__add__)

class P1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj1 = P1("M1", 31)

# prints all object attributes in dictionary format
print(obj1.__dict__)

# documentation of an object: description of attributes and methods
print(help(P1))


# magic/dunder methods
class P2:
    name="M1"
    def __len__(self):
        i = 0
        for ch in self.name:
            i = i+1
        return i
    
    # when we print obj1, then it prints "<__main__.P2 object at 0x000002638ABEEC50>"
    # if we define this function then when we print object then it prints the following
    def __str__(self):
        return f"Name of employee is {self.name}"

obj1 = P2()
print(obj1.name)
print(obj1.__len__())

print(obj1)
'''

def my_generator():
    for num in range(5):
        yield num

gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# below will throw error 
# because it will generate only from 0 to 4
# print(next(gen))


# lru_cache: store result in cache, 
# so that in future same input will provide result quickly
from functools import lru_cache
import time

@lru_cache(maxsize = None)
def func1(n):
    time.sleep(4)
    return n*4

print(func1(10))
print(func1(4))
print(func1(10))
print(func1(6))
