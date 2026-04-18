print("Match Case Statement: [Variable to Match]")
x = int(input("Enter th value of x: "))
#x is variable to match

match x:
    # if x is 0

    case 0:
       print("x is zero")
       #case  with if-condition

    case 4:
        print("case is 4")
           
    case _ if x!= 90:
        print(x, "is not 90")

    case _ if x!= 80:
        print(x, "is not 80") 

    case _:
        print(x)

        # defualt case(will only be matched if the
        #above cases were not matched)  


# Ramesh #Day of the Week Finder 
print("Day of the Week Finder")

day_number = int(input("Enter a number (1-7): "))

match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid number! Enter 1 to 7.") 



# Ramesh #Simple Calculator
print("Simple Calculator") 

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enetr operator (+, -, *, /): ")

match op:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by Zero.")
    case _:
        print("Invalid operator") 

#Ramesh #Month Day Checker
print("Month Day Checker")

month = int(input("Enter Month Number (1-12): "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 Days")
    case 4 | 6 | 9 | 11:
        print("30 Days")
    case 2:
        print("28 or 29 Days (leap year check not included)") 
    case _:
        print("Invalid Month")      

#Ramesh #Grade Evaluator
print("Grade Evaluator") 

grade = input("Enter your grade (A-F): ").upper()

match grade:
    case "A":
        print("Excellent!")
    case "B":
        print("Very Good!")
    case "C":
        print("Good!")
    case "D":
        print("Needs Improvement!")
    case "E":
        print("Poor!")
    case "F":
        print("Failed Poor Minded People!")
    case _:
        print("Invalid Grade.") 



