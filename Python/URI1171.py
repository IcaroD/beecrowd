N = int(input())

num = []
for i in range(N):
    temp = int(input())
    num.append(temp)

X = []
for i in range(N):
        if num[i] not in X:
            X.append(num[i])

X = sorted(X)
for i in range(len(X)):
    print(X[i], "aparece", num.count(X[i])  ,"vez(es)")