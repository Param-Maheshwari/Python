class Employee:
    company = "Microsoft"
    salary = 3600000
    def show(self):
        print(f"Name of company is : {self.company} and salary of employee is : {self.salary}")

# class Programmer:
#     company = "Google"
#     language = "Python"
#     salary = 3600000
#     def show(self):
#         print(f"Name of company is : {self.company} and salary of employee is : {self.salary}")
#     def showLang(self):
#         print(f"Name of company is : {self.company} and he is good with {self.language}")

class Programmer(Employee):
    company = "Google"
    language =  "Python"
    def showLang(self):
        print(f"Name of company is : {self.company} and he is good with {self.language}")

a = Employee()
b = Programmer()

b.show()
b.showLang()