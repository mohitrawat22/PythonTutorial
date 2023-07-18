class Person:
    name="mohit"
    occupation="soft_prof"
    networth=10

    def info(self):
        print(f"name is {self.name} and networth is {self.networth}")

a = Person()
print(a.name, a.occupation)
a.info()

class Person1:

    def __init__(self, n, o, w):
        self.name = n
        self.occupation = o
        self.networth = w
    
    def info(self):
        print(f"{self.name} is {self.occupation}")

a = Person1("mohit", "soft_prof", 10)
a.info()


# decorators

def func1(func3):
    def func2():
        print("Starting the function ...")
        func3()
        print("Ending the function ...")
    return func2

@func1
def greet():
    print("Hello")

greet()

# decorator is same as below
# func1(greet)()

def func4(func3):
    def func2(*args, **kwargs):
        print("Starting the function ...")
        func3(*args, **kwargs)
        print("Ending the function ...")
    return func2

@func4
def add(a,b):
    print(a+b)

add(1,2)

class A1:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"Value is {self._value}")
    
    @property
    def value(self):
        return self._value
    
    @property
    def ten_value(self):
        return 10 * self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value / 10


obj1 = A1(10)
print(obj1._value)
obj1.ten_value = 67
print(obj1.ten_value)
obj1.show()
