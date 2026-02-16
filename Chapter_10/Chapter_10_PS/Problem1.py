class Programmer:
    def __init__(self, name, language, salary):
        self.name = name
        self.language = language
        self.salary = salary
        print(f"The name is {name}.\nThe language is {language}.\nThe salary is {salary}\n\n")


name = input("Enter your name : ")
language = input("Enter your language : ")
salary = int(input("Enter your salary : "))
details = Programmer(name, language, salary)

