with open("Chapter_9/Chapter_9_PS/this.txt") as f :
    content = f.read()

with open("Chapter_9/Chapter_9_PS/copy_of_this.txt", "w") as f :
    f.write(content)