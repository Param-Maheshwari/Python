class Calculator:

    @staticmethod
    def greet(name):
        print(f"Hello {name}")
    
    def __init__(self, num):
        self.sq = (num**2)
        self.cube = (num**3)
        self.sqroot = (num**0.5)
        print(f"The square of number is : {self.sq}\nThe cube of number is : {self.cube}\nThe square root of number is : {self.sqroot}")

name = input("Enter your name : ")
number = int(input("Enter your number : "))
Calculator.greet(name)
details = Calculator(number)

# Use static method in problem 2 to greet user