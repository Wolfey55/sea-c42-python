def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))


num_range = int(input("How many terms shall we evaluate? "))

for i in range(num_range):
    print(fibonacci(i))


def lucas(n):
    l.append(2)
    l.append(1)
    if l <= 2:
        return l
    else:
        return(lucas(l - 1) + lucas(l - 2))


num_range2 = int(input("How many terms shall we evaluate? "))

for i in range(num_range2):
    print(lucas(i))
