myList = [2,5,4,9,6,3]

# squaredList = []
# for i in myList:
#     squaredList.append(i**2)

# Above can be done easily using list comprehension method

squaredList = [i**2 for i in myList]

print(squaredList)