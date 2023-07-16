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
