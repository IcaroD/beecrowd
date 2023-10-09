def valor(maior):
    valor = 0
    if maior < 10:
        valor = 1
    elif maior < 20:
        valor = 2
    elif maior >= 20:
        valor = 3
    return valor

while True:
    try:
            L = []
            N = int(input())
            L = input().split()

            for i in range(N):
                L[i] = int(L[i])

            velo = valor(max(L))

            print(velo)
    except EOFError:
        break