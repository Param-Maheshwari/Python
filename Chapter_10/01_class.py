class Employee:
    language = "Python" # This is a class attribute
    salary = 3600000

param = Employee()
param.name = "Param" # This is an instance (object) attribute
print(param.name, param.language, param.salary)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name, rohan.salary, rohan.language)
 
# Here name is an instance (object) attribute where as salary and language is a class attribute as they directly belong to the class