with open("Chapter_9/Chapter_9_PS/poems.txt") as f:
    content = f.read()
if("Twinkle".lower() in content):
    print("The word twinkle is present")
else:
    print("The word twinkle is not present")