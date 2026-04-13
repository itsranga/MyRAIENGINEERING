def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Olivia", 27)

print("\nCase-2:")
nameAge(27, "Olivia")


def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("\nKeyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')

def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
        
    f2()
f1()

def c1(x): return x*x   
c2 = lambda x : x*x*x  

print(c1(7))
print(c2(7))

def sq_value(num):
    """This function returns the square
    value of the entered number"""
    return num**2

print(sq_value(2))
print(sq_value(-4))


def myFun(x):
    x[0] = 20

lst = [10, 11, 12, 13]
myFun(lst)
print(lst)   

def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)


def factorial(n):
    if n == 0:  
        return 1
    else:
        return n * factorial(n - 1) 
      
print(factorial(5))

import mymodule

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

b = mymodule.person1["name"]
print(b)