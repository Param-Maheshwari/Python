# These features are new in python

dict1 = {'a' : 1, 'b' : 2}
dict2 = {'b' : 3, 'c' : 4}

merged_dict = dict1 | dict2

print(merged_dict)

# Multiple context manager can be used with single "with" function

with(
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    pass
    # Process Files