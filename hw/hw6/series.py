def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n - 1) + fibonacci(n - 2))


num_range = int(input("How many terms shall we evaluate? "))

for i in range(num_range):
    print(fibonacci(i))
