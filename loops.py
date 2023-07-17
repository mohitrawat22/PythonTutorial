num1 = 67

if num1 < 0:
    print("negative")
elif num1 == 0:
    print("zero")
elif num1 < 100:
    print("num1 less than 100")
else:
    print("num1 greater than equal to 100")

# match case
num1 = 100

match num1:
    case 0:
        print("num1 is zero")
    case 50:
        print("num1 is 50")
    case _:
        print("num1 is something else")

match num1:
    case 0:
        print("num1 is zero")
    case 50:
        print("num1 is 50")
    case _ if num1 < 75:
        print("num1 is less than 75")
    case _ if num1 < 100:
        print("num1 is less than 100")
    case _ :
        print("num1 is greater than equal to 100")

# for loop
for i in 'world':
    print(i, end=', ')
print()

for num in range(10):
    print(num, end=" ")
print()
for num in range(3, 10):
    print(num, end=" ")
print()
for num in range(3, 10, 3):
    print(num, end=" ")
print()

# while loop
num=5
while num > 0:
    print(num, end=" ")
    num = num - 1
print()

# we can apply else also
num=5
while num > 0:
    print(num, end=" ")
    num = num - 1
else:
    print()
    print("loop done")
print()

num=5
while True:
    print('This will atleast print once')
    num = num - 1
    if num == 2:
        break;
    else:
        continue;


# works both for while and for loops
# else executes after loop executes completely
for i in range(6):
    print(i)
else:
    print("else block")

# else DOES NOT execute 
# because break did not allow loop to complete completely
for i in range(6):
    print(i)
    if(i == 4):
        break
else:
    print("else block")


# short-hand for if else
a = 40
b = 405
print("a") if a > b else print("=") if (a == b) else print("b")

c=10 if (a > b) else 0
print(c)

# enumerate
list1 = [5,1,8,3,9]
for index, value in enumerate(list1):
    print(index, value)
print()
# indexing usually starts with 0 but now indexing will start from 1
for index, value in enumerate(list1, start=1):
    print(index, value)

# here item is actually a tuple
for item in enumerate(list1):
    print(item)
