n = int(input())

for i in range(0, n):
    x = int(input())

    if x == 0:
        print("NULL")
    elif x % 2 == 0:
        print("EVEN", end=" ")
        if x > 0:
            print("POSITIVE")
        else:
            print("NEGATIVE")
    else:
        print("ODD", end=" ")
        if x > 0:
            print("POSITIVE")
        else:
            print("NEGATIVE")