marks = int(input("Enter your marks : "))

if(int(marks)>90 and int(marks)<=100):
    print("Your grade is Ex.")
elif(int(marks)>80 and int(marks)<=90):
    print("Your grade is A.")
elif(int(marks)>70 and int(marks)<=80):
    print("Your grade is B.")
elif(int(marks)>60 and int(marks)<=70):
    print("Your grade is C.")
elif(int(marks)>50 and int(marks)<=60):
    print("Your grade is D.")
else:
    print("Your grade is F.")