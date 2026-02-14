with open("Chapter_9/Chapter_9_PS/log.txt") as f :
    content = f.read()
if("Python".lower() in content):
    print("The word python is present in log file")
else:
    print("The word python is presemt in log file")