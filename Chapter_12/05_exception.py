try:
    a = int(input("Enter your number : "))
    print(a)

except Exception as e:
    print("Enter a valid number!")

# We can also specify the exception to catch like below

try:
    pass
    # Code
except ZeroDivisionError:
    pass
    # Code
except TypeError:
    pass
    # Code
except :
    pass
    # Code     # All other exceptions are handeled here