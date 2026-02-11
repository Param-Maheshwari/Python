# Function is a block of code that performs a specific task.
# It can be reused multiple times in a program,
# which helps to reduce code duplication and improve readability.

def avg():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    average = (a + b + c) / 3
    print("The average is:", average)

a = avg()
print(a)  # This will print None because the avg() function does not return any value.
avg()