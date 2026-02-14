with open("Chapter_9/Chapter_9_PS/Donkey.txt") as f:
    content = f.read()
if("Donkey" in content):
    content = content.replace("Donkey", "######")

    with open("Chapter_9/Chapter_9_PS/Donkey.txt", "w") as f:
        f.write(content)


# with open("Chapter_9/Chapter_9_PS/Donkey.txt") as f:
#     content = f.read()

# content = content.replace("Donkey", "Horse")

# with open("Chapter_9/Chapter_9_PS/Donkey.txt", "w") as f:
#     f.write(content)
