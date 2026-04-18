#iterating over a (string) 
name = 'Ramesh'
for i in name: 
    print(i)
    #print(i, end=",") 

#iterating over a (list)
colors = ["Red", "Green", "Blue", "Yellow"] 
for color in colors:
    print(color)
    for i in color:
        print(i) 

# range() Ex #Stop
for k in range(5):
    print(k)      #01234
    print(k+1)    #12345
    print(k+2)    #123456

    for k in range(1,9):
        print(k)    #12345678
        print(k+1)  #123456789

#Ex #Start
for k in range(1, 201):
    print(k) 

#Explore 3rd one #Step range() by own 

#Ramesh 
wilds = ["Lion", "Tiger", "Cheeta", "Hyneas"]
for wild in wilds:
    print(wilds)
    for i in wilds:
        print(wilds) 


#Python While loop

count = 5
while(count > 0):
    print(count)
    count = count - 1


i = 0
while(i <= 3):
    print(i)
    i = i+1
    print("Done with the loop")  

i = int(input("Enter the number: "))
while(i <= 90):
    i = int(input("Enter the number: "))
    print(i)

print("Done with the loop")

#Else with while loop
x = 5
while(x > 0):
    print(x) 
    x = x-1
else:
    print("counter is 0")

count = 5 
while(count > 0):
    print(count)
    count = count - 1
else:
    print("I am inside else")


#Break Statement 
for i in range ( 1, 101, 1):
    print(i, end="  ")
    if (i == 50):
        break

    else:
        print("Mississippi")

print("Thank You") 


for i in range(12):
    if(i == 10):
        break
    print("5 X", i+1, "=", 5* (i+1))
print("Loop Ko chodkar nikal gaya")


# Break means leave the Loop
# Continue means leave the iteration 

#Continue Statement

for i in [2, 3, 4, 6, 8, 0]:
    if (i%2 != 0):
        continue 
    print(i) 


for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue 
    print("5 X", i, "=", 5* i)


# Do While Loop Emulate 

i = 0
while True:
    print(i)
    i = i+1
    if(i%100 == 0):
        break

# For loop practice topics
# Print numbers from 1 to 100
for i in range(100):
    i = i+1
    print(i)

# Print even numbers between 1 to 50
for num in range(1,51): 
    if num % 2 == 0:
        print(num)

# Start from 2, go to 50, and step by 2
for num in range(2, 51, 2):
    print(num)

# Multiplication table of any number 
for n in range(1,13): 
    print("8 X", n, "=", 8**n) 

for m in range(1,13):
    print("90 X", m, "=", 90*m)

for b in range(1,11):
    print("100/",b, "=", 100/b) 


# Check if a number is prime or not 

print("Check if a number is prime")
num = int(input("Enter the number:"))
if num <= 1:
    print("Not a prime number.")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break 

if is_prime:
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")

# Prime Numbers from 1 to 100

print("Prime numbers between 1 to 100 are:")

for num in range(2, 101): # From 2 to 100 
    is_prime = True
    for i in range(2, int(num**0.5)+1): #Efficient check up to square root
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end= " ")



# While loop Practicing 
#1. Print numbers until user types exit
#2. Guess the secret number (number guessing game)
#3. Sum of digits of a number
#4. Check if a number is a palindrome
#5. Keep asking for password until it’s correct
#6. Print a countdown timer
#7. Reverse a number (e.g., 123 → 321)
#8. Find the greatest digit in a number
#9. Create a login system with 3 attempts
#10. While loop to simulate a menu-driven program 


# 1st Solution
# Print numbers until user types exit

while True:
    user_input = input("Enter a number (or type 'exit' to stop):") 

    if user_input.lower() == "exit":
        print("Exited the loop.")
        break
    else: 
        try:
            number = float(user_input)
            print("You entered:", number)
        except ValueError:
            print("Invalid input! Please enter a number or 'exit'.")


# Create a login system with 3 attempts
# Set the correct credentials
correct_username = "admin"
correct_password = "1234"

# Maximum attempts allowed
max_attempts = 3 
attempts = 0

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password ")

    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts += 1 
        print(f"Incorrect login. Attempts left: {max_attempts - attempts}")
if attempts == max_attempts:
    print("Access denied. Too many incorrect attempts.")

# Keep asking for password until it's correct
correct_password = "python123"
while True:
    entered_password = input("Enter your password: ")

    if entered_password == correct_password:
        print("Access granted ")
        break
    else:
        print("Incorrect password. Try again.")

        


