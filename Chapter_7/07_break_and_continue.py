# Break will exit the loop immediately when a certain condition is met.
for i in range(100):
    if i == 46:
        break  # This will exit the loop when i is equal to 46
    print(i)

# Continue will skip the current iteration and move to the next iteration of the loop when a certain condition is met.
for i in range(100):
    if i == 46:
        continue  # This will skip the rest of the code in the loop for i equal to 46 and move to the next iteration
    print(i)