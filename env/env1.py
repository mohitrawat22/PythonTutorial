def func1():
    print("welcome 1")

def func2():
    print("welcome 2")
    
num2 = 6

# whenever some toher .py files import this file then "welcome 1" will print twice
# func1 call from parent file and func1 call from current file
func1()

print(__name__)
if __name__ == '__main__':
    func2()