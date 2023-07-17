'''
try:
    num1 = int(input("enter the number: "))
    print(num1)
except Exception as e:
    print(e)

# if we dont want to use e
try:
    num1 = int(input("enter the number: "))
    print(num1)
except:
    print('Invalid input')


try:
    num1 = int(input("enter the number: "))
    print(num1)
    a = [1,2]
    print(a[num1])
except ValueError:
    print('Invalid value')
except IndexError:
    print('Invalid index')


# even if you return, finally always execute
def func1():
    try:
        num1 = int(input("enter the number: "))
        print(num1)
        return 1
    except:
        print('Invalid input')
        return 0
    finally:
        print('I always execute')

print(func1())
'''

# custom exceptions
num1 = int(input("enter the number: "))
if num1 < 5 or num1 > 9:
    raise ValueError("Number is invalid")