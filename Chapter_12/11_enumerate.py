l = [12,85,94,111]

# index = 0
# for item in l:
#     print(f"The items number at index {index} is {item}")
#     index += 1


# Above can be done easliy using enumerate
for index, item in enumerate(l):
    print(f"The items number at index {index} is {item}")