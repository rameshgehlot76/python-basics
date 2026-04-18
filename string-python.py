name = "RAMESH"
friend = "Rohan"
anotherFriend = 'Noha'
apple = '''He said,
Hi Tiger 
hey I am good
"I want to eat an apple'''  

print("Hello," + name)
print(apple)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# print(name[6]) # Throws an error 
print("Lets use a for loop") 
for character in apple:
    print(character)

fruit = "Mango"
mangolen = len(fruit)
print(mangolen)


print(fruit[0:4]) # including 0 but not 4
print(fruit[1:4]) # including 1 but not 4
print(fruit[:5])
print(fruit[0:-3])
print(fruit[:len(fruit)-3])
print(fruit[-1:len(fruit) -3])
print(fruit[-3:-1])

# Quick quize:
nm = "Harry"
print(nm[-4:-2])

# Strings are immutable
a = '!!!Ramesh !!!!!!!!!!!! Ramesh'

"""upper(), lower()
The upper() method converts a string to upper case.
The lower() method converts a string to lower case."""
print(len(a))
print(a) 
print(a.upper())
print(a.lower())

#The rstrip() removes any trallinng characters.
print(a.rstrip("!"))

'''The replace() method replaces all occourances
# of a string with another string.'''
print(a.replace("Ram", "Sur"))

'''The split() method splits the given string at 
the specified instance and returns the seprated
strings as list items.'''
print(a.split(" ")) 

"""The capitalize() method turns only the first 
character of the string to uppercase and the rest
other characters of the string are turned to lowercase.
The strings has no effect if the first character
is already uppercase."""
blogHeading1 = 'introduction to tate'
print(blogHeading1.capitalize()) 

blogHeading2 = "introduction tO TATE"
print(blogHeading2.capitalize())

#The center() method aligns the string to the
#center as per the parameters given by the user.
str6 = "Who is Better$$$"
print(str6)
print(str6.center(40))
#We can also provide padding character. It will
#fill the rest of chharacter provided by the user.
print(str6.center(40,"."))

'''The count() method returns the number of times
the given value has occurred within the given string.'''
print(a.count("Ramesh"))

'''The endswith() method checks if the string ends
with a given value. If yes then return True,else
return False.'''
print(str6.endswith("$$$"))
# True
#We can even also check for a value in between the
#string by providing start and end index positions.
print(str6.endswith("is", 2, 6)) 
#True # ho is 

"""The find() method searches for the first occirrence
of the given value and  returns the index where it is present.
 If given value is absent from the string then return -1."""
print(str6.find("Who"))
# 1 
print(str6.find("Tate")) 
#-1

'''The index() method searches for the first occurrence
of the given value and returns the index where it is present.
If given value is absent from the string then raise
an exception.'''
print(str6.index("Better"))

'''The isalnum() method returns True only if the entire string
only consists of A-Z,a-z,0.9. If any other characters
or punctuations are present, then it returns False.'''
print(str6.isalnum())
#True  #False

'''The isalpha() method returns True only if the entire
string only consists of A-Z,a-z. If any other characters or punctuations
numbers(0-9) are present, then it returns False.'''
print(str6.isalpha())
#True  #False

'''The islower() method returns. True if all the 
characters in the string are lower case, else it 
returns False.'''
str7 = "hello world"
print(str7.islower())
#True  #False

'''The isprintable() method returns True if all the
values within the given string are printable, if not,
then return False.'''
str7 = "Welcome here"
print(str7.isprintable())
#True  #False

"""The isspace() method returns True only and
only if the string contains white spaces, else returns
False."""
str7 = "         "    #using Spacebar 
print(str7.isspace())
str8= '           '   #using Tab
print(str8.isspace()) 
#True  #True 

"""The istitle() returns True only if the first
letter of each word of the string is capitalized,
else it returns False."""
str7 = "World Health Organization"
print(str7.istitle())  #True
str8 = "veridian stream"
print(str8.istitle())  #False

'''The isupper() method returns True if all the characters
in the string are upper case, else it returns False.'''
str7 = "WORLD HEALTH ORGANIZATION"
print(str7.isupper())
#True

'''The startswith() method checks if the string with 
a given value. If yes then returns True,else return False.'''
str7 = "Python is a Interpreted Language"
print(str7.startswith("Python")) 
#True 

'''The swapcase() method changes the characters casing
of the string. Upper case are converted to lower case
and lower case to the upper case.'''
str7 = "Python is a Interpreted Language"
print(str7.swapcase())
#pYTHON IS A iNTERPRETED lANGUAGE

"""The title() method capitalizes each letter of the
word within the string."""
str8 = "My name is nashh"
print(str8.title())
# My Name Is Nashh 