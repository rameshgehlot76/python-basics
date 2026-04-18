# Implicit Typecasting 
# Python automaticaly converts 
# a to int 
a = 7
print(type(a))

# Python automaticaly converts b to float
b = 3.0
print(type(b))

# Python automaticaly converts c to float as it is a float addition 
c = a + b
print(c)
print(type(c))

# Explicit Typecasting 
string = "15"
number = 7 
string_number = int(string) # throws an errow if the string is not a valid integer
sum = number + string_number 
print("The Sum of both the number is:",sum)


