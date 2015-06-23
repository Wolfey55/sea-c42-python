def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))

print(fibonacci(0))


def lucas(n):
    # function to evaluate lucas series
    if n < 1:
        return 2
    if n == 1:
        return n
    else:
        return(lucas(n - 1) + lucas(n - 2))

print(lucas(0))


# function to evaluate both fibonacci and lucas series
def sum_series(n, a=0, b=1):
    # evaluates fibonacci series
    if n < 1:
        return a
    elif n == 1:
        return b
    else:
        return(sum_series(n - 1, a, b) + sum_series(n - 2, a, b))


