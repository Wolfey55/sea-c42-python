def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))


num_range = int(input("How many terms shall we evaluate? "))

for i in range(num_range):
    print(fibonacci(i))


def lucas(n):
    # function to print lucas series
    if n < 1:
        return 2
    if n == 1:
        return n
    else:
        return(lucas(n - 1) + lucas(n - 2))

# input from user
num_range2 = int(input("How many terms shall we evaluate? "))

# print the range set by the user
for i in range(num_range2):
    print(lucas(i))
