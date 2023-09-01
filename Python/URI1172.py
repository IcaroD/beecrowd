x = []

for i in range(10):
    temp = int(input())
    x.append(temp)

for i in range(10):
    if x[i] <= 0:
        x[i] = 1

for i in range(10):
    print("X["+ str(i) +"] =", x[i])