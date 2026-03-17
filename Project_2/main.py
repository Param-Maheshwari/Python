from random import randint
n = randint(1, 100)
a = -1
count = 0
while(a != n):
    a  = int(input("Enter your number : "))
    if(a<n):
        print("Higher number please")
        count += 1
    elif(a>n):
        print("Lower number please")
        count += 1

print(f"You guessed the number {n} in {count} attempt")