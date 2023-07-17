#def double(x):
#    return x*2

# above function can be written as
double = lambda x: x*2

print(double(5))

add = lambda x,y: x+y
print(add(4, 5))

# passing anonymous function as argument
def appl(func1, value):
    return func1(value) + 4

print(appl(lambda x: x**2, 5))

# map
# print square of all numbers in list
# normal way
list1 = [1,2,3,4]
def square(x):
    return x*x
list2 = []
for i in list1:
    list2.append(square(i))
print(list2)

# map way
list3 = list(map(square, list1))
print(list3)

# another way using lambda
list4 = list(map(lambda x: x**2, list1))
print(list4)


# filter
def filter_func(x):
    return x > 2
list5 = list(filter(filter_func, list1))
print(list5)

list6 = list(filter(lambda x : x > 2, list1))
print(list6)


from functools import reduce
sum = reduce(lambda x,y: x+y, list1)
print(sum)
