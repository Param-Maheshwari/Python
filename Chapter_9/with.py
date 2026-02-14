# f = open("Chapter_9/file.txt")
# print(f.read())
# f.close

# The same can be written using "with" statement like this : -

with open("Chapter_9/file.txt") as f:
    print(f.read())

# You dont have to explicitely close the file