def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))


num_range = int(input("How many terms shall we evaluate? "))

for i in range(num_range):
    print(fibonacci(i))


def lucas(n):
    # function to evaluate lucas series
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


# function to evaluate both fibonacci and lucas series
def sum_series(n, a=0, b=1):
    # evaluates fibonacci series
    if a == 0 and b == 1:
        if n <= 1:
            return n
        else:
            return(sum_series(n - 1) + sum_series(n - 2))

    # evaluates lucas series
    elif a == 2 and b == 1:
        if n < 1:
            return 2
        if n == 1:
            return n
        else:
            return(sum_series(n - 1) + sum_series(n - 2))

# input from user
num_range3 = int(input("How many terms shall we evaluate? "))

# prints the range set by user
for i in range(num_range3):
    print(sum_series(i))

