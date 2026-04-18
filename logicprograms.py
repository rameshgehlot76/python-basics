#1. Check Even or Odd
num = int(input("Enter a number: ")) 
if num % 2==0: 
    print("Even")
else:
    print("Odd") 


#2. Find Largest of Three Numbers
a = int(input("Enter a: "))
b = int(input("Enter b: ")) 
c = int(input("Enter c: ")) 

if a > b and a > c:
    print("Largest is", a)  
elif b > c:
    print("Largest is", b)
else:
    print("Largest is", c) 


#3. Check Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year") 
else:
    print("Not a Leap Year")


#4. Reverse a Number
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num //= 10 

print("Reversed: ", rev) 



#5. Task1 Code 
num = int(input("Enter a number: "))  

if num < 0:
    print("Negative number") 
elif num % 2 == 0:
    print("Even")
else:
    print("Odd")   


#6. Task2 Code 
num = int(input("Enter a number: ")) 

def check_positive_negative_zero(num):
    if num > 0: 
        print("Positive Number") 
    elif num < 0:
        print("Negative Number") 
    else:
        print("Zero")      

def check_even_odd(num): 
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number") 

check_positive_negative_zero(num)
check_even_odd(num) 

#7. Task3 Code 

num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0: 
    print("FizzBuzz") 
elif num % 3 == 0: 
    print("Fizz")
elif num % 5 == 0: 
    print("Buzz")
else:
    print(num) 

#8. Task4 Code 
num = int(input("Enter a number: ")) 

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number") 

is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime Number")
else:
    print("Not a Prime Number") 

