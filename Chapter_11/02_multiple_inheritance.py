class Employee:
    company = "Microsoft"
    salary = 3600000
    def show(self):
        print(f"Name of company is : {self.company} and salary of employee is : {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language your language is : {self.language}")

class Programmer(Employee, Coder):
    company = "Google"
    language =  "Python"
    def showLang(self):
        print(f"Name of company is : {self.company} and he is good with {self.language}")

a = Employee()
b = Coder()
c = Programmer()

c.show()
c.printLanguage()
c.showLang()