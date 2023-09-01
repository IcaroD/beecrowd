fib = [0, 1]
x = []

T = int(input())

for i in range(T):
    temp = int(input())
    x.append(temp)

for i in range(1, 61):
    temp = fib[i] + fib[i-1]
    fib.append(temp)

for i in range(T):
    print("Fib("+str(x[i])+") =", fib[x[i]])
