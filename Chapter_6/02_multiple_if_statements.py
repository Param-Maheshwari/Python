age  = int(input("Enter your age: "))

#If statement number 1

if(age%2==0):
    print("Your age is an even number.")

# End of if statement number 1


#If statement number 2

if(age>=18):
    print("You are eligible to vote.")

elif(age<0):
    print("Invalid age entered.")

elif(age==0):
    print("You are a newborn baby.")

else:
    print("You are not eligible to vote.")

# End of if statement number 2

print("End of the program.")

# if can be alone statement, but elif and else must always be preceded by an if statement.