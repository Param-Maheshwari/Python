num = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
num4 = int(input("Enter number 4 : "))

if(num>num2 and num>num3 and num>num4):
    print("The greatest number is : ",num)

elif(num2>num and num2>num3 and num2>num4):
    print("The greatest number is : ",num2)

elif(num3>num and num3>num2 and num3>num4):
    print("The greatest number is : ",num3)

else:
    print("The greatest number is : ",num4)
