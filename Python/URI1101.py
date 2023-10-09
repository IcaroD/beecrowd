def laco(maior, menor):
    soma = 0
    for i in range(menor, maior+1):
        print(i, end=" ")
        soma += i
    print("Sum=%d" %soma)

linha = input().split()
m = int(linha[0])
n = int(linha[1])

while m > 0 and n > 0:
    if m < n:
        temp = n
        n = m
        m = temp

    laco(m, n)

    linha = input().split()
    m = int(linha[0])
    n = int(linha[1])