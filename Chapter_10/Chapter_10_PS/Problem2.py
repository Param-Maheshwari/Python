class Calculator:
    def __init__(self, num):
        self.sq = (num**2)
        self.cube = (num**3)
        self.sqroot = (num**0.5)
        print(f"The square of number is : {self.sq}\nThe cube of number is : {self.cube}\nThe square root of number is : {self.sqroot}\n")

number = int(input("Enter your number : "))
details = Calculator(number)
