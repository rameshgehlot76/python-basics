def calculateGmean(a,b):    
    mean = (a*b)/(a+b)
    print(mean)
def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a,b):
    pass

a = 9 
b = 8
isGreater(a,b)
calculateGmean(a,b)
#gmean1 = (a*b)/(a+b)
#print(gmean1)

c = 8
d = 74
isGreater(c,d) 
#gmean2 = (c*d)/(c+d)
#print(gmean2)
calculateGmean(c,d)   

# Ramesh
def isLessers(x,y):
    if(x<y):
        print("First number is Lessers")
    else:
        print("Second number is Lessers or equal") 

x = 4
y = 8 
isLessers(x,y)

fname = str(input("Enter Your Name: ") )
def greetname(name):
    print("Hello", name ,"Welcome!") 

greetname(fname) 

# Funtion to return the square of a number

num = int(input("Enter the number:")) 
def square(num):
    return num * num 

result = square(num)
print("The square is:", result)

# Sum of Two Numbers
x = int(input("Enter the first number:"))
y = int(input("Enter the second number:")) 
def add_number(x,y):
    numbers = (x + y) 
    print(numbers) 

add_number(x,y)   

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Example usage
result = add_numbers(7, 3)
print("The sum is:", result)
 
# Functions to check if a number is even
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

number = int(input("Enter Number:"))
if is_even(number):
    print(number, "is Even")
else:
    print(number, "is ODD")

# Funtions to find the maximum of two numbers
def max_of_two(x,y):
    if x > y:
        return x 
    else:
        return y 

num1 = int(input("Frist Number:"))
num2 = int(input("Second Number:")) 
print("The maximum is:", max_of_two(num1,num2))

#Functions Arguments and RETURN Statements
# Deafualt Argument 
def name(fname, mname = "Jammes", lname= "Cummins"): 
    print("Hello", fname, mname, lname) 

    name("Pattrick") 

# 1 
# Write a function that takes a number and returns whether
# it is positive, negative, or zero. 
def return_n(a): 
    if a > 0: 
        print("The number is positive")
    elif a < 0: 
        print("The number is negative") 
    else:
        print("The number is Zero")  

a = int(input("Enter the number: ")) 
return_n(a)

# 2 
# Checks if a number is positive or negative 
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# Example usage 
num = int(input("Enter a number: "))
result = check_number(num) 
print("The number is:", result) 

# 3
# Write a function that takes two numbers and returns the larger one.
def larger_num(a,b): 
    if a > b : 
        return a  
    else:
        return b 

a = int(input("First Number: "))
b = int(input("Second Number: "))
results = larger_num(a,b) 
print(results,"is the larger one")

# 4 
# Write a function that takes a string and returns its length 
# (without using len()). 
def string_length(s):
    count = 0 
    for char in s:   # loop through each character 
        count += 1   # increase count 
    return count 

# Example usage 
text = input("Enter a string: ") 
print("Length of string is:", string_length(text))

# 5 
# Write a function that converts kilometers to miles. 
print("                            ")  
print("1 kilometer = 0.621371 miles") 
print("                            ")
def km_to_miles(km): 
    miles = km * 0.621371 
    return miles 

# Example usage 
km = float(input("Enter distance in kilometers: ")) 
print(f"{km} kilometers = {km_to_miles(km)} miles") 

# 6  
# Write  a function that takes a number and returns its 
# multiplication table. 
print("                                      ")
print("Get Multiplication Table of any number") 
print("                                      ")  

def multiplication_table(n):
    table = []            # store results in a list 
    for i in range(1,11): # table from 1 to 10 
        table.append(f"{n} x {i} = {n * i}") 
    return table 

# Example usage 
num = int(input("enter a number: "))
result = multiplication_table(num) 

# Print the table 
for line in result:
    print(line)  

# 7
# Function that takes a name as input and print "Hello, <name>!". 
def hello_n(name):
    print("Hello", name) 
    return name 

fname = input("Enter Your Name: ")  
hello_n(fname)   

# 8 
# Absolute value of a number
def absolute_value(n):
    if n < 0:
        return -n    # make it positive 
    else:
        return n 

# Example usage
num = int(input("Enter a number: ")) 
print("Absolute value is:", absolute_value(num)) 

# 9 
# Two number and their products 
def product(a,b):
    return a * b 

# Example usage
x = int(input("Enter first number: "))
y = int(input("Enter second number: ")) 

print("The product is:", product(x,y))

# 10 
# Square root of a Number 
print("Square Root")
def square_root(n):
    return n * n 

# Example usage
n = int(input("Enter a Number: ")) 
print("The Square Root of", n,"is", square_root(n)) 

# 11 
# Cube root of a Number
print("Cube Root")  
def cube_root(n):
    return n * n * n

# Example usage
n = int(input("Enter a Number: "))
print("The Cube Root of", n,"is", cube_root(n))

# 12 
# Print each Element one by one 
print("List Elements")
def print_list_elements(lst):
    for element in lst: 
        print(element) 

# Example usage
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
print_list_elements(numbers)

# 13 
# Person is eligible to vote (age>18) 
print("Checks if you are eligible to vote") 
def vote_el(p): 
    if p >= 18:
        print("You are Eligible to Vote") 
    else:
        print("You are *NOT* Eligible to Vote") 

# Example usage 
p = int(input("Enter Your Age: ")) 
vote_el(p) 

# 14 
# Returns the largest one among three numbers 
def largest_num(a,b,c): 
    if a >= b and a >= c:   
        return a 
    elif b >= a and b >= c: 
        return b  
    else:
        return c 

# Example usage 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: ")) 

print("The largest number is:", largest_num(a, b, c)) 

# 15 
# Returns the last character of a string 
def last_char(s):
    if s == "":     # check for empty string
        return "String is empty" 
    for ch in s:    # loop through each character 
        last = ch   # keep updating 
    return last 

# Example usage 
text = input("Enter a string: ") 
print("Last character is:", last_char(text))


# 16 
# Simple Calculator using functions 

# Functions definitions 
def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b 

def divide(a, b):
    if b == 0:
        return "Error! Division by Zero." 
    return a / b 

# Main Program 
print("----- Simple Calculator -----") 
print("Select operation:") 
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide") 

choice = input("Enter choice (1/2/3/4): ") 

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: ")) 

if choice == "1":
    print("Result:", add(num1, num2)) 
elif choice == "2":
    print("Result:", subtract(num1, num2)) 
elif choice == "3":
    print("Result:", multiply(num1, num2)) 
elif choice == "4":
    print("Result:", divide(num1, num2)) 
else:
    print("Invalid choice!")


# 17 
# Student Grade Calculator  

# Functions to calculate total marks 
def calculate_total(marks):
    return sum(marks) 

# Function to calculate percentage 
def calculate_percentage(total, subjects):
    return total / subjects 

# Function to get grade based on percentage
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "c"
    elif percentage >= 50:
        return "D"
    else:
        return "F" 

# Main program
print("----- Student Grade Calculator -----")

subjects = int(input("Enter number of subjects: "))
marks = [] 

for i in range(subjects):
    score = float(input(f"Enter marks for subject {i+1}: ")) 
    marks.append(score) 

total = calculate_total(marks) 
percentage = calculate_percentage(total, subjects) 
grade = get_grade(percentage) 


print("\n----- RESULT -----") 
print("Total Marks:", total) 
print("Percentage:", round(percentage, 2), "%") 
print("Grade:", grade)



# 18
# Number Guessing Game Project 

import random

# Function to generate a random number
def get_random_number():
    return random.randint(1, 100)   # number between 1 and 100

# Function to check the guess
def check_guess(user_guess, secret_number):
    if user_guess < secret_number:
        return "Too low! Try again."
    elif user_guess > secret_number:
        return "Too high! Try again."
    else:
        return "Correct! You guessed it!" 


# Main program 
print("----- Number Guessing Game -----") 
secret_number = get_random_number()
attempts = 0 

while True:
    guess = int(input("Enter your guess (1-100): ")) 
    attempts += 1
    result = check_guess(guess, secret_number)
    print(result) 

if guess == secret_number:
    print(f"You guessed the number in {attempts} attempts 🎉")


# 19 
# Mini Banking System with Multiple Users + PIN Login + Transaction History

# Dictionary to store accounts {account_number: {"pin": pin, "balance": balance, "history": []}} 
accounts = {
    "101": {"pin": "1234", "balance": 1000.0, "history": []},
    "102": {"pin": "2222", "balance": 500.0, "history": []},
    "103": {"pin": "3333", "balance": 2000.0, "history": []}, 

} 

def create_account(account_number, pin):
    if account_number in accounts:
        return "Account already exists!" 
    else:
        accounts[account_number] = {"pin": pin, "balance": 0.0, "history": []}
        return f"Account {account_number} created successfully with balance ₹0.0"

def login(account_number, pin):
    if account_number in accounts and accounts[account_number]["pin"] == pin:
        return True 
    else:
        return False 

def deposit(account_number, amount):
    accounts[account_number]["balance"] += amount 
    accounts[account_number]["history"].append(f"Deposited  ₹{amount}") 
    return f"₹{amount} deposited successfully! Current balance: ₹{accounts[account_number]["balance"]}" 

def withdraw(account_number, amount):
    if amount > accounts[account_number]["balance"]:
        return "Insufficient balance!"  
    else:
        accounts[account_number]["balance"] -= amount 
        accounts[account_number]["history"].append(f"Withdraw ₹{amount}") 
        return f"₹{amount} withdrawn successfully! Current balance: ₹{accounts[account_number]["balance"]}"

def check_balance(account_number):
    return f"Your current balance is: ₹{accounts[account_number]["balance"]}"

def show_history(account_number):
    history = accounts[account_number]["history"] 
    if not history:
        return "No transaction yet."
    else:
        return "\n".join(history)


# Main Program
print("----- Welcome to Mini Banking System -----")

while True:
    print("\nChoose an option: ") 
    print("1. Create Account") 
    print("2. Login")
    print("3. Exit") 

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        acc = input("Enter new account number: ")
        pin = input("Set a 4-digit PIN: ")
        print(create_account(acc, pin)) 
    
    elif choice == "2":
        acc = input("Enter account number: ")
        pin = input("Enter PIN: ") 

        if login(acc, pin):
            print(f"\nLogin successful! Welcome, Account {acc} 🎉") 

            while True:
                print(f"\nBanking Menu:") 
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance") 
                print("4. Transaction History")
                print("5. Logout") 
                
                option = input("Enter choice (1/2/3/4/5): ") 

                if option == "1":
                    amt = float(input("Enter amount to deposit: ")) 
                    print(deposit(acc, amt)) 
                
                elif option == "2":
                    amt = float(input("Enter amount to withdraw: "))
                    print(withdraw(acc, amt)) 

                elif option == "3":
                    print(check_balance(acc)) 

                elif option == "4":
                    print("\n--- Transaction History ---") 
                    print(show_history(acc)) 

                elif option == "5":
                    print("Logged out successfully ✅")
                    break 

                else: 
                    print("Invalid option!") 

        else: 
            print("Invalid account number or PIN ❌") 

    elif choice == "3":
        print("Thank you for using Mini Banking System 😊")
        break 

    else:
        print("Invalid choice! Please try again.")






# 20 
# To-Do List (Basic Console App) 

tasks = []  # list to store tasks 

def add_task(task):
    tasks.append(task)
    return f"✅ Task added: {task}" 

def view_task():
    if not tasks:
        return "📂 No tasks in the list!"
    result = "\n--- Your To-Do List ---\n"
    for i, task in enumerate(tasks, start=1):
        result += f"{i}. {task}\n"
    return result 

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number -1)
        return f"❌ Task removed: {removed}"
    else:
        return "⚠️ Invalid task number!"


# Main Program 
print("----- Welcome to To-Do List App -----") 

while True:
    print("\nChoose an option: ")
    print("1. Add Task") 
    print("2. View Task")
    print("3. Remove Task")
    print("4. Exit") 

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter task: ") 
        print(add_task(task)) 

    elif choice == "2":
        print(view_task()) 

    elif choice == "3":
        try:
            num = int(input("Enter task number to remove: ")) 
            print(remove_task(num)) 
        except ValueError:
            print("⚠️ Please enter a valid number!") 

    elif choice == "4":
        print("👋 Exiting To-Do List App. Goodbye!")
        break 


    else: 
        print("⚠️ Invalid choice! Please try again.")



# Calendar in Python 
import calendar
yy = 2012  # year 
mm = 11    # month 
# display the calendar 
print(calendar.month(yy, mm))


# Internet speed checker 
import speedtest 

st = speedtest.Speedtest()
dl = st.download()
up = st.upload() 

print("Download Speed:", dl/1024/1024, "kbs")
print("Upload Speed:", up/1024/1024, "kbs")


# Phone Number Tracker 

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

def track_number(phone_number):
    try:
        # Parse number with country code (e.g. +91 for India, +1 for USA)
        parsed_number = phonenumbers.parse(phone_number)

        # Check validity
        valid = phonenumbers.is_valid_number(parsed_number)
        possible = phonenumbers.is_possible_number(parsed_number)

        # Get details
        country = geocoder.description_for_number(parsed_number, "en")
        sim_carrier = carrier.name_for_number(parsed_number, "en")
        time_zones = timezone.time_zones_for_number(parsed_number)

        # Print results
        print(f"\n📞 Phone Number: {phone_number}")
        print(f"✅ Valid: {valid}")
        print(f"❓ Possible: {possible}")
        print(f"🌍 Country/Region: {country}")
        print(f"📡 Carrier: {sim_carrier if sim_carrier else 'Unknown'}")
        print(f"⏰ Timezones: {', '.join(time_zones)}")

    except Exception as e:
        print("Error:", e)


# ------------------------- 
# Example Usage
# -------------------------
if __name__ == "__main__":
    number = input("Enter phone number with country code (e.g. +919876543210): ")
    track_number(number)
# END


# Whatsapp Message to Anyone 
import pywhatkit as kit
kit.sendwhatmsg("+918007844912", "Hello RAMESH this is an Automated message sent using Python!", 16,45) 
# Replace with actual number and time
# Note: The time is in 24-hour format (HH, MM). Make sure to set it a few minutes ahead of the current time.


# Python program to generate password
import random 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbols = "!@#$%^&*()_+"

all = lower + upper + num + symbols
length = 16 
password = "".join(random.sample(all,length))
print(password) 
# END 



# QR Code Generator in Python
import qrcode
data = "Name Ramesh Gehlot"  # URL or text data 
qr = qrcode.make(data)
qr.save("RameshCummins.png")
print("QR Code Generated!")
# END 

# Barcode Generator in Python
import barcode
from barcode.writer import ImageWriter
code_data = "918007844912"  # Example data
code_type = "ean13"  # Barcode type (e.g., ean13, upc, code39, etc.)
barcode_class = barcode.get_barcode_class(code_type)
my_barcode = barcode_class(code_data, writer=ImageWriter())
my_barcode.save("MyBarcode")
print("Barcode Generated!")
# END 


# Enumerate Functions in python 
marks = [ 12, 56, 32, 98, 12, 45, 1, 4]

# without Enumerate 
'''index = 0 
for mark in marks:
    print(mark)
    if(index == 3):
        print("Harry, awesome!")
    index +=1''' 

# using Enumerate Functions 
for index, mark in enumerate(marks): 
    print(mark)
    if(index == 3):
        print("Harry, awesome!") 

# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango'] 
for index, fruit in enumerate(fruits):
    print(index, fruit) 

# Changing the start index
fruits = ['apple', 'banana', 'mango'] 
for index, fruit in enumerate(fruits, start=1): 
    print(index, fruit) 


fruits = ['apple', 'banana', 'mango'] 
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')  

# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue') 
for index, color in enumerate(colors, start=2):
    print(index, color) 

# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(f'{index+2}: {s}') 



# NEW TOPIC 
# Virtual Environment  in Python 

# Create a virtual environment 
##  python -m venv myenv 

# Activate the virtual environment (Linux/macOS)
## source myenv/bin/activate

# Activate the virtual environment (Windows) 
## myenv\Scripts\activate.bat    [noteee]

### if using powershell 
#  myenv\Scripts\activate.ps1 

# Activate the virtual environment (Windows)(PowerShell) 
##  myenv\Scripts\activate.ps1 

# Deactivate the virtual environment 
## deactivate  

# Output the list of installed packages
## pip freeze 

# Install the packages listed in the requirements.txt file
## pip install -r requirements.txt 


# Next Topic 
# Importing in python 
# How importing in python works

import math
result = math.sqrt(9) 
print(result)  # Output: 3.0 

# direct use of sqrt function from math 
from math import sqrt 
result = sqrt(9) 
print(result)  # Output: 3.0 

#You can also import multiple funtions or variables at once by separating them with a comma:
from math import sqrt, pi 
result = sqrt(9) 
print(result) # Output: 3.0 

print(pi) # Output : 3.141592653589793 

# The "as" keyword
import math as m 
from math import pi, sqrt as s 
result = m.sqrt(9) * m.pi 
print(result)  #Output: 3.0

print(m.pi)  # Output : 3.141592653589793 
  
# The "dir" function 
import math 
print(dir(math)) 
print(math.nan, type(math.nan))
# Output will be of all list of functions and variables in it  

# importing from my file 
import ramesh as rh 
#from ramesh import welcome, ramesh
from ramesh import * 
print(dir(ramesh))  
rh.welcome()
print(rh.ramesh) 





# Learned OS Module in python  
# OS Module  


# Next Topic 
# Global and Local variables 

# Global var  #Ex  
x = 5 
y = "Hello, World!"

# Local var #Ex 

def hello():
    x = 5
    y = 1 
    print(f"The local x is {x}") 
    print("Hello harry")

print(f"The global x is {x}") 
hello() 

x = 5 
print(f"The global x is {x}")

# Ex2 
x = 10 # global variable 

def my_function():
    global x   # change global var in func 
    x = 4
    y = 5 # local variable 
    print(y) 

my_function() 
print(x) 
# print(y)  # this will cause an error because y is a 
# local variable and is not accessible outside of the function 






























