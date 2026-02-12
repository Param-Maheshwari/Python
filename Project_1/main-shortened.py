import random

'''
rock = 1
paper = 0
sissor = -1

'''

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice : ")
youDict = {"r": 1, "p": 0, "s": -1}
reverseDict = {1: "rock", 0: "paper", -1: "sissor"}
you = youDict[youStr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("Its draw")
# else:
#     if(computer == 0 and you == 1):  (computer-you) = -1
#         print("You loose")
#     elif(computer == 0 and you == -1):   (computer-you) = 1
#         print("You win")
#     if(computer == 1 and you == 0):   (computer-you) = 1
#         print("You win")
#     elif(computer == 1 and you == -1):   (computer-you) = 2
#         print("You loose")
#     if(computer == -1 and you == 1):   (computer-you) = -2
#         print("You win")
#     elif(computer == -1 and you == 0):   (computer-you) = -1
#         print("You loose")
#     else:
#         print("Something went wrong!")

# Below logic is based on (computer-you) calculation

else:
    if((computer-you) == -1 or (computer-you) == 2):
        print("You loose!")
    else:
        print("You win!")