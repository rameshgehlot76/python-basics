# Python Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets.
# *Note: Set items are unchangeable, but you can remove items and add new items.
# Sets do not allow duplicate values.
# Example
thisset = {"apple", "banana", "cherry"}
print(thisset)

info = {"Carla", 25, True, 60.5, 25} # A set can contain different data types
print(info) # Duplicates will be ignored 

# Get the length of a set
print(len(thisset))
# Note: The order of the items in a set is unpredictable, so you cannot refer to an item by index or key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
# Example
for x in thisset:
  print(x)
print("banana" in thisset) # Check if "banana" is present in the set 
# To add one item to a set use the add() method.
thisset.add("orange")
print(thisset) 

# To add more than one item to a set use the update() method.
thisset.update(["mango", "grape", "pineapple"])
print(thisset)

# To remove an item in a set, use the remove(), or the discard() method. 

thisset.remove("banana") # if the item to remove does not exits, remove will raise an error
print(thisset) 
thisset.discard("apple") # if the item to remove does not exits, discard will NOT raise an error 
print(thisset) 

# You can also use the pop(), method to remove an item but this method will remove the last item.
x = thisset.pop() # remove a random item
print(x)
print(thisset) 

# The clear() method empties the set
thisset.clear() 
print(thisset) 

# The del keyword will delete the set completely 
del thisset
# print(thisset) # this will raise an error because the set no longer exists 

print("New ITEMS")    
# Join two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3} 
set3 = set1.union(set2) # or set1.upadate(set2)
print(set3) 
# The set() constructor
set4 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(set4) 

# Example of set methods
setA = {"apple", "banana", "cherry"}
setB = {"google", "microsoft", "apple"}
print(setA.intersection(setB)) # returns a set that contains the item that exists in both setA and setB
print(setA.symmetric_difference(setB)) # returns a set that contains all items from both sets, except items that are present in both sets

print(setA.union(setB)) # returns a set that contains all items from both sets, duplicates are excluded
print(setA.isdisjoint(setB)) # returns True if no items in setA are present in setB

print(setA.issubset(setB)) # returns True if all items in setA are present in setB
print(setA.issuperset(setB)) # returns True if all items in setB are present in setA
print(setA.difference(setB)) # returns a set that contains the items that are in setA but not in setB


print(setA.update(setB)) # adds items from setB into setA
print(setA)

print(setA.intersection_update(setB)) # removes the items from setA that are not present in setB
print(setA) 

if "apple" in setA:
  print("Yes, 'apple' is in the setA") 
else:
  print("No, 'apple' is NOT in the setA") 

setC = setA.copy() # or setC = set(setA) 
print(setC)

setC.clear() 
print(setC) 
# Empty set 
harry = set() 
print(type(harry)) 

print("End of Sets.py")


# Python Dictionaries
# Python Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
# *As of python version 3.7, dictionaries are oredered. In Python 3.6 and earlier, dictionaries are unoredered.
# Dictionaries are written with curly brackets, and have keys and values.
# Example 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
} 
print(thisdict) 
print(len(thisdict)) # Get the length of a dictionary
print(type(thisdict)) # Print the data type of a dictionary

# Accessing Items
x = thisdict["model"] # or  
x = thisdict.get("model")
x = thisdict.keys() # returns a view object that displays a list of all the keys in the dictionary
x = thisdict.values() # returns a view object that displays a list of all the values in the dictionary
x = thisdict.items() # returns a view object that displays a list of a dictionary's key:value pairs
print(x) 

# Change Values
thisdict["year"] = 2018 # or
thisdict.update({"year": 2020}) 
print(thisdict)

# Adding items 
thisdict["color"] = "red" # or
thisdict.update({"color": "blue"}) 
print(thisdict)

# Removing items
thisdict.pop("model") # or 
thisdict.popitem() # removes the last inserted item

del thisdict["brand"] # or 
# del thisdict # delete the dictionary completely
thisdict.clear() # empties the dictionary
print(thisdict) 

# Loop through a dictionary
for x in thisdict:
  print(x) # prints the keys
  print(thisdict[x]) # prints the values 
  

for x in thisdict.values():
  print(x) # prints the values

for x in thisdict.keys():
  print(x) # prints the keys 

for x, y in thisdict.items():
  print(x, y) # prints both the keys and values

# Copy a dictionary
mydict = thisdict.copy() # or
mydict = dict(thisdict)
print(mydict) 

# Nested Dictionaries 
myfamily = {
  "child1": {
    "name": "Emil",
    "year": 2004
  },
  "child2": {
    "name": "Tobias",
    "year": 2007
  },
  "child3": {
    "name": "Linus",
    "year": 2011 
  } 
}
print(myfamily) 
print(myfamily["child2"]["name"]) 
print("End of Dictionary.py") 


