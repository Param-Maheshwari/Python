with open("Chapter_9/Chapter_9_PS/this.txt") as f :
    content = f.read()

with open("Chapter_9/Chapter_9_PS/copy_of_this.txt") as f :
    content_2 = f.read()

if(content == content_2):
    print("Content of both the files is same")
else:
    print("Content of both the files is not same")