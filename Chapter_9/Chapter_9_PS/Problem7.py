with open("Chapter_9/Chapter_9_PS/log.txt") as f :
    content = f.readlines()

lineno = 1
for line in content :
    if("Python".lower() in line):
        print(f"The word python is present in log file, line no : {lineno}")
        break
    lineno += 1
else:
    print("The word python is NOT present in log file")