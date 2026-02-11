def got(a,b,c):
    if(a>b and a>c):
        print("a is the greatest number.")
    elif(b>a and b>c):
        print("b is the greatest number.")
    else:
        print("c is the greatest number.")

a = int(input("Enter value of a : "))
b = int(input("Enter value of b : "))
c = int(input("Enter value of c : "))

got(a,b,c)