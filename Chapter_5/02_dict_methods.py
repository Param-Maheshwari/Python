marks = {
    "Param" : 33,
    "Varnika" : 36,
    "list" : [1,2,5,7,9],
    0 : "Param"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Param" : 34, "Vanshika" : 50})
# print(marks)

print(marks.get("Param2")) # Output : None
print(marks["Param2"]) # Returns an error