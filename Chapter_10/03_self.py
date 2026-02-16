class Employee:
    language = "Python" # This is a class attribute
    salary = 3600000

    def getInfo(self):
        print(f"The language is {self.language}, the salary is {self.salary}.")

    @staticmethod
    def greet():
        print("Good Morning")

param = Employee()
param.language = "C++" # This is an instance (object) attribute
param.greet()
param.getInfo()  # Employee.getInfo(param)