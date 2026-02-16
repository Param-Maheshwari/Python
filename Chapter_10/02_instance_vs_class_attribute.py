class Employee:
    language = "Python" # This is a class attribute
    salary = 3600000

param = Employee()
param.language = "C++" # This is an instance (object) attribute
print(param.language, param.salary)

# Instance attribute takes more preference over class attributes during assignment & retrieval.