class Employee:
    a = 1

class Manager(Employee):
    b = 2

class Programmer(Manager):
    c = 3

o = Employee()
print(o.a)
# print (o.b) # Gives error bcz b not present in Employee

o = Manager()
print(o.a,o.b)

o = Programmer()
print(o.a,o.b,o.c)