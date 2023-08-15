fib = [0, 1]

n = int(input())

for i in range(2, n):
    next = fib[i-1] + fib[i-2]
    fib.append(next)

for i in range(0, n):
    print(fib[i], end="")
    if fib[i] == fib[n-1]:
        print(end="\n")
    else:
        print(end=" ")
