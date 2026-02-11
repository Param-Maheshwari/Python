# Sum of first n natural numbers

# def sum_of_n(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum = sum + i
#         i += i
#     return sum

# With recursion
def sum_of_n(n):
    if(n == 0):
        return 0
    return sum_of_n(n-1) + n

n = int(input("Enter the number : "))

print(f"Sum of first {n} natural number is : {sum_of_n(n)}")