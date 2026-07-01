import ramesh
ramesh.welcome() 
print(ramesh.ramesh) 

# Next  
# File handling in python 

# Reading a file   
f = open('myfile.txt', 'r') # r for read  
#f = open('myfile.txt', 'w') # w for write 
# print(f) 
text = f.read()  # read or write  
#text = f.write()     
print(text) 
f.close()  

# Writing a file 
f = open('myfile.txt', 'a') 
f.write('Hello, world!') 
f.close() 

with open('myfile.txt', 'a') as f:
    f.write("Hey I am inside with") 


# Next Topic 
# Python Class and Objects 

'''A class is a blueprint or a template for creating objects,
providing initial values for state (member variables or attributes),
and implementations of behavior (member functions or methods). 
The user-defined objects are created using the class keyword.'''

class Details: 
    name = "Rajesh"
    age = 24

class Person:
    name = "Ramesh"
    occupation = "AI/ML Engineer"
    networth = 3600000
    def info(self):
        print(f"{self.name} is a {self.occupation}") 

# Creating an Object 
'''Object is the instance of the class used to access
the properties of the class Now lets create an object
of the class'''  

a = Person() 
bb = Person() 
c = Person()   # this are 3 different objects 

b = Details() 

# update class.  a = Person() 
# a.name = "Harry"  
# a.occupation = "Software Developer"
# a.networth = 50 

print(a.name, a.occupation, a.networth) 
a.info() 

b.name = "Shubham"
b.age = 18
print(f"{b.name} age is {b.age}") 

bb.name = "Nikita"
bb.occupation = "HR" 
bb.info() 
a.info()

c.info()   # It will print deafult value 



# Next Topic 
# Instance var Vs  Class variable 

'''In Python, variables can be defined at the instance level.
Understanding the difference between these types of variables 
is crucial for writing efficient and maintainable code.'''

# Class var 
'''Class variables are defined at the class level and are 
shared among all instance of the class.'''

class MyClass:
    class_variable = 0   #Class Variable 

    def __init__(self):
        MyClass.class_variable += 1 

    def print_class_variable(self):
        print(MyClass.class_variable) 

obj1 = MyClass() 
obj2 = MyClass() 

obj1.print_class_variable()  # Output: 2   
obj2.print_class_variable()  # Output: 2 



class Employee:
    companyName = "Apple"  # Class Variable 
    noOfEmployees = 0
    def __init__(self, name):
        self.name = name 
        self.raise_amount = 0.02
        Employee.noOfEmployees += 1

    def showDetail(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount}") 

# Employee.showDetail(emp1)
emp1 = Employee("Harry") 
emp1.raise_amount = 0.3
emp1.companyName = "Apple India" # Instance Variable
emp1.showDetail() 



# Time module in Python 
# time.time() 

import time
# print(time.time()) 


def usingWhile():
    i = 0
    while i<50000:
        i = i + 1 
        print(i) 

def usingFor():
    for i in range(50000):
        print(i) 

init = time.time() 
usingFor()
t1 = (time.time() - init) 

init = time.time()  
usingWhile() 
print(time.time() - init)
print(t1) 

#By this method the output will paused for 5 seconds and then executed
print(4)
time.sleep(5) 
print("This is printed after 5 seconds") 

# time.strftime() 
t = time.localtime() 
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S" , t) 
print(formatted_time) 
# Output: 2025-10-20 17:06:55 








