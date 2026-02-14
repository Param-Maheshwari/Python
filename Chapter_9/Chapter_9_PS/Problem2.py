import random

def game():
    print("You are playing the game")
    score = random.randint(1,50)
    #Fetch the highscore
    with open("Chapter_9/Chapter_9_PS/Hi-score.txt") as f:
        hiscore = f.read()
    if(hiscore != ""):
        hiscore = int(hiscore)
    else:
        hiscore = 0
    
    print(f"Your score is : {score}")
    if(score>hiscore):
        with open("Chapter_9/Chapter_9_PS/Hi-score.txt", "w") as f:
            f.write(str(score))
    return score

game()    