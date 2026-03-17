a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if (b == 0):
    raise ZeroDivisionError("Our program does not divide number by 0")
else:
    print(f"The division of a/b is : {a/b}")

# Raise will crash the program