def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Param", "Rohan", "Varnika", "an"]

print(rem(l, "an"))

# Will look at this again later