marks = int(input("Enter your marks in subject 1 : "))
marks2 = int(input("Enter your marks in subject 2 : "))
marks3 = int(input("Enter your marks in subject 3 : "))

if((marks+marks2+marks3)/3 > 40 and marks>=33 and marks2>=33 and marks3>=33):
    print("Congratulations! You have passed the exam.")

else:
    print("Sorry! You have failed the exam.")
