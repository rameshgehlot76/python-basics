a = int(input("Enter your age: "))
print("Your age is:", a) 

print(a>18)
print(a<=18)
print(a==18)
print(a!=18) 

if(a>=18):
    print("You will get licence")
    print("Yes")

else:
    print("You will not get licence")
    print("No")

print("Yay!") 
# HARRY 


# RAMESH
r = str(input("Enter is raining outside Yes/No:"))

if(r == "Yes"):
    print("You will not go for lectures")

else:
    print("You will go for the lectures")

#Ramesh  
a = str(input("Today U have holiday in your school? Yes/No:"))

if(a=="Yes"):
    print("You can watch IndvsEng TestMatch")

else:
    print("You will not watch IndvsEng TestMatch")

# Conditional operators
# >, <, >=, <=, ==, (!=)Not equal to 

#Harry 
applePrice = 10
budget = 200
if(budget - applePrice > 50):
    print("Alexa, add 1Kg Apples to the cart.")

elif (budget - applePrice > 70):
    print("Its okay you can buy")

else:
    print("Alexa, do not add Apples to the cart.")

#elif

num = int(input("Enter the value of num:")) 

if(num < 0):
    print("Number is negative.")

elif (num == 0):
    print("Number is Zero.")

elif (num == 555):
    print("Number is FIVEERS")

else:
    print("Number is positive.")

print("I am Getting Now")

#Ramesh 
num = int(input("Enter How many Runs you have scored today:")) 

if(num == 0):
    print("Off YOu have get one DUCK")

elif (num < 50):
    print("GOOD RUNS YOU HAVE SCORED")    

elif (num == 50):
    print("WoW You have score 50 Runs its your 1st Half Centuary")

elif (num > 50 and num < 100):
    print("Excellent Its a very Good Enning") 

elif (num == 100):
    print("CENTUARY 100")

elif (num > 100 and num < 200):
    print("Congratulations For The First Madian Centuary")  

elif (num == 200):
    print("Its a DOUBLE CENTUARY")       

else:
    print("You have not played a cricket Ever") 
 
print("!BHooyaa")


#Nested if else if if 

num = int(input("Enter the value of num:"))

if(num < 0):
    print("Number is negative.")

elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")   

#Ramesh #Grading System

print("Input a Student's marks and determine their Grade")

num = int(input("Enter Student Marks:"))

if(num > 90):
    print("You has got A Grade" )
    print("Excellent Performance")

elif(num > 75):
    print("You have got B Grade") 
    print("Very Good YOU have Performed")

elif(num > 50):
    print("You have got C Grade")  
    print("Can Do Better")

elif(num > 40):
    print("You have got D Grade")
    print("Just PASS")

else:
    print("ATKT ATKT FAILLL FAILURE")
    print("Submit your ReExam Fee Noww")   


# Python - else in Loop 
# for loop 
# Ex1 
for i in range(5): 
    print(i) 

else:
    print("Sorry no i") 


# Ex2 
for i in []:
    print(i) 

else:
    print("Sorry no i")


# Ex3 
for i in range(6):
    print(i) 
    if i == 4:
        break 
    
else:
    print("Sorry no i") 

# while loop 
i = 0 
while i<7:
    print(i) 
    i = i+1 
    #if i == 4:
    #   break

else:
    print("Sorry no i") 

# Ex
for x in range(5):
    print("iteration no {} in for loop".format(x+1)) 
else:
    print("else block in loop")
print("Out of loop") 



# Error Handling in Python 
# Exception Handling in Python 

a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ") 
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}") 
except Exception as e:
    print(e) 
except:
    print("Invalid Input!")  

print("Some imp lines of code")
print("End of program") 

# Ex2 
try:
    num = int(input("Enter an integer: "))
    a = [6, 3] 
    print(a[num]) 
except ValueError:
    print("Number entered is not an integer. ") 

except IndexError:
    print("Index Error") 



#Finally Clause 
#Ex1 

def func1(): 
 try:
     l = [1, 5, 6, 7]
     i = int(input("Enter the index: ")) 
     print(l[i]) 
     return 1
 except:
     print("Some error occurred") 
     return 0 

 finally:
      print("I am always executed")
    # print("I am always executed") 

x = func1() 
print(x) 


#Raising Custom Errors 
# Ex1 
a = int(input("Enter any value between 5 and 9")) 

if(a<5 or a>9): 
    raise ValueError("Value should be between 5 and 9") 

   


# Short Hand if-else statement 
# If...Else in One Line 
a = 2
b = 338
print("A") if a > b else print("B") 

# One line if else statement, with 3 conditions: 
a = 33000
b = 3303
print("A") if a > b else print("=") if a == b else print("B") 

print(9) if a>b else ""

c = 9 if a>b else 0  
print(c) 

# Another Example 
# result = value_if_true if condition else value_if_false 

'''The shorthand syntax can be a convenient way to write single if-else
statements, especially when you want to assign a value to a variable based
on a condition. However, it's not suitable for more complex situation where 
you need to execute multiple statements or perform more complex logic. In 
those cases, it's best to use the full if-else syntax.'''

