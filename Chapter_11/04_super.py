class Employee:
    def __init__(self):
        print("This is a constructor of Employee.")
    a = 1

class Manager(Employee):
    def __init__(self):
        print("This is a constructor of Manager.")
    b = 2

class Programmer(Manager):
    def __init__(self):
        super().__init__()
        print("This is a constructor of Programmer.")
    c = 3

o = Programmer()
print(o.a,o.b,o.c)