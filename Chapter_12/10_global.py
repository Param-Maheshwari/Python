a = 69 # This is a global variable

def fun():
    global a # Thsi will tell python to  change the global value of a
    a = 5
    print(a)

fun()
print(a)