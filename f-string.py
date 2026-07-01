# f-Strings in python 
# String formating in python 

country = "India"
name = "Nick" 
letter = "Hey my name is {1} and I am from {0}" 
print(letter.format(country,name))  
# the above line is imp for string formating 

print(f"Hey my name is {name} and I am from {country}")
print(f"Hey my name is {{name}} and I am from {{country}}")

price = 49.09999
txt = (f"For only {price:2f} dollars!")  
print(txt) 
print(txt.format(price)) 

print(type(f"{2 * 30}")) 
print(f"{2 * 30}") 

# Debugging helper using f-strings 
x = 10 
y = 20
sum_result = x + y 

# f-string automatiically prints variables with  their  name and values
print(f"x={x}, y={y}, sum={sum_result}") 

# you can use = inside f-strings: 
x = 10
y = 20 
print(f"{x=}, {y=}, {x+y=}") 

# DocString and PEP-8 in Python
# DocString in python

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2) 

square(5)  
print(square.__doc__)  

# Docstring must be after function name only not somewhere else
# it will not work 
# the second line of the function is not comment
# it is a known DocString  

# PEP-8 
# Just an "Eastern Egg" in python 
# python 
# import this 
"""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


# Recursion in python 

# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1 

# factorial(n) = factorial(n-1) 
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) 

print(factorial(5)) 
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1   
 
# Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0 
# f(1) = 1 
# f(2) = f(1) + f(0) 
# f(n) = f(n-1) + f(n-2) 
# 0 1 1 2 3 5 8 13 21 34 

# Fibonacci sequence program 
'''This program is For efficiency, we use iteration (the first program) or
memoization to speed up recursion.'''

# number of terms
n = int(input("Enter the number of terms: ")) 

# first two terms 
a, b = 0, 1 
count = 0 

print("Fibonacci sequence: ") 
while count < n:
    print(a, end=" ") 
    # update values 
    a, b = b, a + b 
    count += 1

# New program  # Our solution main program 
'''The recursive approach is simple but slower for large n,
because it repeats calculations many times.'''

# Recursive functions for fibonacci 
def fibonaccii(n):
    if n <= 1:
        return n 
    else:
        return fibonaccii(n-1) + fibonaccii(n-2) 

# number of terms
n = int(input("Enter the number of terms: ")) 

print("Fibonacci sequence: ")
for i in range(n):
    #print(fibonaccii(i), end= " ")  
    print(fibonaccii(i)) 


# Optimized Fibonacci using memoization
def fibonacci(n, memo={}):
    if n in memo:       # If result already in memo, return it
        return memo[n]  
    if n <= 1:          # Base case 
        memo[n] = n  
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo) 
    return memo[n] 

# number of terms 
n = int(input("Enter the number of terms: ")) 

print("Fibonacci sequence: ")
for i in range(n):
    #print(fibonacci(i), end=" ") 
    print(fibonacci(i))  

