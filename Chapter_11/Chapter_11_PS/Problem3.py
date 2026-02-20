class Employee :
    salary = 500
    increment = 10

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary) - 1) * 100

e = Employee()
# print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 550
print(e.increment)


# new salary = old salary +  old salary * (increment/100)
# new salary = old salary  (1 + (increment/100))
# increment = ((new salary/old salary) - 1) * 100