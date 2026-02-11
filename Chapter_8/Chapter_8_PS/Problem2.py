def ctf(celsius):
    f = (9/5*(celsius)) + 32
    return f

c = int(input("Enter the value in celsius : "))

print(f"Temp in fahrenheit is : {ctf(c)}")