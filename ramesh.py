def welcome():
    print("Hey you are welcome my friend") 

ramesh = "MEN"

# if __name__ == "__main__" in python 

''' The if __name__ == "__main__" idiom is a common pattern used in python
scripts to determine whether the script is being run directly or being imported
as a module into another script.. '''  

print(__name__) 
if __name__ == "__main__": 
    welcome()  


