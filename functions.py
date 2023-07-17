def add(a, b):
    print(a+b)

add(4, 5)

# function which does not do anything
def add1(a, b):
    pass

def subtract(a, b):
    print(a-b)

subtract(5, 3)
subtract(a=3, b=5)

def multiple(a, b, c=2):
    print(a*b*c)

multiple(4,3,3)
multiple(4,3)

# if you want to pass list, use *
def average(*nums):
    sum = 0
    for i in nums:
        sum = sum + i
    print(sum/len(nums))

average(5,7,3,1)

# if you want to pass dictionary, use **
def func1(**names):
    print(type(names))
    print(names["fname"]+" "+names["lname"])

func1(fname="mohit", lname="rawat")

# we can have multiple return staements, 
# but only first will be valid but there will be no errors
def add1(a, b):
    return a+b
    return 5

print(add1(3,4))


# pass function as an argument
def func1(a, b):
    return a+b

def func2(func1, a, b):
    return 6+func1(a, b)

print(func2(func1, 2, 3))