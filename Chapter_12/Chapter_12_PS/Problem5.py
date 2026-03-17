num = int(input("Enter a number : "))

table = [num * i for i in range(1,11)]

with open ("Chapter_12/Chapter_12_PS/tables.txt", "a") as f:
    f.write(f"Table of {num} : {str(table)} \n")