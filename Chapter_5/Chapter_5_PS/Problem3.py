s = set()

s.add(20)
s.add(20.0)
s.add('20')

print(s)

# In python 20 = 20.0, so the first two items are considered the same and only one
# of them is stored in the set. The string '20' is different, so it is also stored in the set.
# Therefore, the output will be: {20, '20'}