s = {8, 7, 12, "Param", [1,2]}

# In python, sets cannot contain mutable items like lists.
# So, the list [1,2] cannot be added to the set and will be ignored.
# The output will be: {8, 7, 12, 'Param'}
# Also you cannot update the list in the set, because it is not hashable.