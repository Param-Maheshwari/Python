words = ["Donkey", "animals", "transport", "humans"]

with open("Chapter_9/Chapter_9_PS/words.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("Chapter_9/Chapter_9_PS/words.txt", "w") as f:
    f.write(content)