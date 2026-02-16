class Employee:
    language = "Python" # This is a class attribute
    salary = 3600000

    def __init__(self, name, language, salary): # Dunder method which calls itself automatically, not all dunder methods call itself
        self.name = name  # Creating an instance attribute over here
        self.language = language
        self.salary = salary
        print("I am creating an object.")

    def getInfo(self):
        print(f"The language is {self.language}, the salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good Morning")

param = Employee("Param", "C++", 4000000)
# param.name = "Param"
print(param.name, param.language, param.salary)

# ram = Employee()