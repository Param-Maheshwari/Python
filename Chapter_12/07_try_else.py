try:
    a=int(input("Hey, Enter a number : "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else!")

# If 'try' runs successfully then it will go inside 'else' otherwise not