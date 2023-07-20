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


# inheritence
class C1:
    def __init__(self, name, id):
        self.name = name
        self.id =id

    def func1(self):
        print(f"func1 - name id {self.name} and id is {self.id}")

# C2 inherits C1
class C2(C1):
    def func2(self):
        print(f"func2 - name id {self.name} and id is {self.id}")

emp1 = C1("m1", 1)
emp1.func1()
emp2 = C2("m2", 2)
emp2.func1()
emp2.func2()


# access modifiers

# _ for protected
# __ for private
class C3:
    def __init__(self):
        # double underscore(__) means attribute is private
        self.__name = "m3"

emp3 = C3()
# cannot be accessed directly
# print(emp3.__name)

# can be accessed indirectly
print(emp3._C3__name)

class C4:
    def __init__(self):
        # double underscore(__) means attribute is private
        self._name = "m4"
    
    def _func1(self):
        return "func1"

class C5(C4):
    pass

obj1 = C4()
obj2 = C5()

print(obj1._name)
print(obj1._func1())
print(obj2._name)
print(obj2._func1())


# static methods
class C6:
    def __init__(self, n):
        self.num = n

    def addToNum(self, n1):
        return self.num + n1
    
    @staticmethod
    def addStatic(a, b):
        return a+b

obj1 = C6(5)
print(obj1.addToNum(6))
print(obj1.addStatic(4,5))
print(C6.addStatic(4,5))

# instance variable
class C7:
    comp = "Apple"

    def __init__(self, name):
        self.name = name

    def showDetails(self):
        print(f"name is {self.name} and company name is: {self.comp}")

# if object is used to assign comp, then value stored in object is printed
obj1 = C7("A")
obj1.comp = "A1"
obj1.showDetails()

obj2 = C7("B")
obj2.comp = "B1"
obj2.showDetails()

# if object is NOT used to assign comp, then comp value of class is printed
obj3 = C7("C")
obj3.showDetails()


# class method
class C8:
    comp = "Apple"

    def __init__(self, name):
        self.name = name
    
    def showDetails(self):
        print(f"name is {self.name} and company name is {self.comp}")

    def changeCompWithoutClassMethod(self, newComp):
        self.comp = newComp

    @classmethod
    def changeCompWithClassMethod(self, newComp):
        self.comp = newComp

obj1 = C8("M1")
obj1.showDetails()
# change comp
# but only for instance, not for class
obj1.changeCompWithoutClassMethod("Apple 1")
obj1.showDetails()

# class variable is still the same
print(C8.comp)

# variable changed for class variable
obj1.changeCompWithClassMethod("Apple 2")
obj1.showDetails()
# now class variable is changed
print(C8.comp)


# super method
class P1:
    def parent_method(self):
        print("Parent Method ...")

class C1(P1):
    def child_method(self):
        super().parent_method()
        print("Child Method ...")

obj1 = C1()
obj1.child_method()


# super in constructor
class P2:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class C2(P2):
    def __init__(self, name, id, age):
        # points to class P2 constructor
        super().__init__(name, id)
        self.age = age

obj1 = C2("M1", 1, 31)
print(obj1.name)
print(obj1.id)
print(obj1.age)

# overriding
class P3:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    
    def area(self):
        print(self.length * self.breadth)

class C3(P3):
    def __init__(self, s):
        super().__init__(s,s)

rec = P3(3,4)
rec.area()

sq = C3(4)
sq.area()

# operator overloading
class P4:
    def __init__(self, i,j,k):
        self.i=i
        self.j=j
        self.k=k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, obj):
        return f"{self.i+obj.i}i + {self.j+obj.j}j + {self.k+obj.k}k"

obj1 = P4(3,4,5)
print(obj1)

obj2 = P4(4,5,6)
print(obj2)

# this will throw error saying that : unsupported operand types for +
# you need to define what + means
# so, add a function __add__ and define what + means
print(obj1+obj2)


# single inheritence
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species = 'Dog')
        self.breed = breed
    
    def make_sound(self):
        print("Dog sound")

obj1 = Dog("D1", "Dog1")
obj1.make_sound()

obj2 = Animal("D2", "Dog2")
obj2.make_sound()
print()


# Multilevel inheritence

class Animal1:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print(f"Name is: {self.name}")
        print(f'Species is: {self.species}')

class Dog1(Animal1):
    def __init__(self, name, breed):
        Animal1.__init__(self, name, species = 'Dog')
        self.breed = breed
    
    def make_sound(self):
        Animal1.make_sound(self)
        print(f"Breed is: {self.breed}")

class GoldenRet(Dog1):
    def __init__(self, name, color):
        Dog1.__init__(self, name, breed="Golden_Ret")
        self.color = color
    
    def make_sound(self):
        Dog1.make_sound(self)
        print(f"Color is: {self.color}")

obj1 = GoldenRet("D1", "Black")
obj1.make_sound()
print(GoldenRet.mro())


# Multiple inheritence
class P5:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"{self.name}")

class P6:
    def __init__(self, dancer):
        self.dancer = dancer

    def show(self):
        print(f"{self.dancer}")

# if function is common in both P5 and P6 
# then method of the class inherited first will be called
class P7(P5, P6):
    def __init__(self, name, dancer):
        self.name = name
        self.dancer = dancer

obj1 = P7("M1", "R1")
obj1.show()
print(P7.mro())


