# Python Lists 
lst1 = [1,2,3,4,5,6]
lst2 = ["Red","Green","Blue"] 
print(lst1)
print(lst2)

# Ex.2
details = ["Abhijeet", 18, "FYBScIT", 9.8] 
print(details) 
# As we can see, a single list can contain items of different data types. 

marks = [3,5,6, "Harry", True, 33, 44, 555 ,666]  
print(marks) 
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
#print(marks[5]) 

colors = ["Red","Green","Blue","Yellow","Green"] 
#          [0]   [1]      [2]     [3]      [4]  
print(colors[2])
print(colors[4])
print(colors[0]) 

# Negative Indexing:
print("Negative Indexing:")  
colors = ["Red","Green","Blue","Yellow","Green"] 
#           [-5]   [-4]    [-3]   [-2]    [-1]   
print(colors[-1])
print(colors[-3])
print(colors[-5]) 

print("MARKS") 
# marks = [3,5,6, "Harry", True, 33, 44, 555 ,666]
print(marks[-3]) #Negative index
print(marks[len(marks)-3]) #Positive index
print(marks[5-3]) #Positive index
print(marks[2]) #Positive index 

#Check item present in the list 
colors = ["Red","Green","Blue","Yellow","Green"]
if "Yellow" in colors:
     print("Yellow is present.")
else:
    print("Yellow is absent.") 

#Range of index 
#Syntax: 
#        listName[start :end :jumpIndex]  

animals = ["rat","dog","bat","mouse","Pig","horse","donkey","goat","cow"] 
print(animals[3 : 7]) 
print(animals[ -1 : -6 ]) 

print(marks) 
print(marks[1:-1])
print(marks[1:4:2])
print(marks[:]) 


print("Animals")
print(animals[4:]) 
print(animals[-4:]) 

print(animals[:4])
print(animals[:-5]) 

#Printing alternate values 
print(animals[::2]) 
print(animals[-8:-1:2]) 

print(animals[1:8:3]) 

#List comprehension 
#Accepts items with the small letter "o" in the new list 
print("Names With")
names = ["Milo","Sarah","Bruno","Anastasia","Rosa"] 
namesWith_o = [item for item in names if "o" in item] 
print(namesWith_o) 

names = ["Milo","Sarah","Bruno","Anastasia","Rosa"] 
namesWith_o = [item for item in names if(len(item)> 4)] 
print(namesWith_o)

# Python Lists Methods
# 
# l.sort() 
# l.sort(reverse = True)
# num.reverse()
# print(num.index("3"))
#                ("7")  
# print(num.count(5)) 
# num.copy() 
# num.append("9") 
# num.insert(1,"5") 
# num.extend(numbers)
# print(num + numbers) 

# l.sort()
print(".sort()") 
num = [1,2,3,4,5,6,7,8,9,0]
num.sort()
print(num) 

# l.sort(reverse = True)
print(".sort(reverse = True)") 
num.sort(reverse = True) 
print(num) 

# num.reverse()
print(".reverse()") 
num.reverse() 
print(num) 

# num.index() 
print(".index()") 
print(num.index(3)) 
print(num.index(7))  

# count()
print(".count()")
print(num.count(5))
print(num.count(9)) 
print(num) 

# copy()
print(".copy()")
new_num = num.copy()
print(num)
print(new_num)

# append() 
print(".append()") 
num.append(11)
print(num)

# insert() 
print(".insert()")
num.insert(1,8)
print(num) 

# extend() 
print(".extend()") 
num = [1,2,3,4,5,6,7,8,9,0] 
numbers = [11,22,33,44,55,66,77] 
num.extend(numbers) 
print(num)

# Concatenating two lists  
print("Concatenating list")  
print(num+numbers)  

# Practicing the lists 

print("Using .extend()") 

print("Lists Of Fruits And Vegetables To Bring")

fruits = ["Apples", "Bananas", "DragonFruit", "Guava", "PineApple", "Avocado", "pomegranate"] 

vegetables = ["Beetroot", "Spanish", "Bottleguard", "Cucumber", "Tomatoo", "Patatos", "Turmeric"]  

fruits.extend(vegetables) 
print("Merged Lists:", fruits)


print("Using .remove()")

peoples = ["Family", "Friends", "Relatives", "Ramesh Gehlot"]  
peoples.remove("Ramesh Gehlot")    
print("After Removed peoples:", peoples) 
#print(peoples) 

popped_item = fruits.pop(2) 
print("After pop:", peoples) 
print("Popped item was:", popped_item)

# Lists of favorite movies 
movies = ["Inception", "Avengers", "Intersteller", "The Dark Knight", "Titanic"]

# Printing movies one by one using a loop 
print("My Favorite Movies:") 
for movie in movies:
    print(movie) 

for i in range(len(movies)):
    print(f"{i+1}. {movies[i]}") 

# List of 10 numbers 
numbers = [12,7,9,24,36,41,50,63,72,85] 

print("Even numbers are:") 
for num in numbers:
    if num % 2 == 0:   # check if a number is divisible by 2
        print(num) 

# Another Way 
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

# List of numbers 
numbers = [12,45,7,89,34,56,23,91,10] 

# Find largest and smallest using built-in-functions
largest = max(numbers)
smallest = min(numbers) 

print("Numbers in the list:", numbers)
print("Largest number is:", largest)
print("Smallest number is:", smallest)


# {Tuples} in Python 
# {Tuples} are {imutable} 
tup = (1,2,3) 
tup1 = ("Red","Colors","Green") 
print(tup)
print(tup1) 

details = ("Ram",17,"FYOOP",9.8) 
print(details) 

print(details[1]) 
print(details[-1]) 

# Check for item: 
print("Check for item ")
if "Ram" in details:
    print("Yes") 
else:
    print("No") 

# Range of indexes in {Tuples}
print("Range of index") 
print(details[1:4:2]) 
print(details[:])   
print(details[1:3])   
print(details[-3:-1]) 

# Manipulating Tuples
print("Manipulating Tuples") 

countries = ("Spain","Italy","India","England","Germany",)
temp = list(countries) 
temp.append("Spain")   # add item
temp.pop(3)            # remove item 
temp[2] = "Spain"      # change item 
countries = tuple(temp) 
print(countries)  

grocerry = ("Rice","Dal","Sugar","Flour","Colgate","Butter","Choklate","Salt","Milk","Red Chilly") 
items = list(grocerry) 
items.append("Butter")                 # added items 
items.pop(3)                           # removed items
#items[5] = "Toothpaste","Peanuts"     # changed items 
items.count("Rice")  
res = len(items) 
#items.index(5)  
  
if "Red Chilly" in items:
    print("Yess Red Chilly is There") 
else: 
    print("No Red Chilly is not there") 
#items.insert(1,"Food Color") 
grocerry = tuple(items) 
print(grocerry)  

student = ("Ramesh Khimaram Gehlot", 20, "CS") 
name, age, branch, = student
print(name, age, branch) 






 



