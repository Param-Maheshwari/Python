def myFunc():
    print("This is my function!")

myFunc()

if __name__=="__main__":
    # If this code is directly executed by the file it's present in
    print("We are directly running this code")
    myFunc()
    print(__name__)

# __name__=="__main__" ------> This prevents it from running in other files that imported this module