tabela ={1001: 1.5, 1002: 2.5, 1003: 3.5, 1004: 4.5, 1005: 5.5}

n = int(input())

soma = 0
for i in range(n):
    linha = input().split()
    num = int(linha[0])
    qte = int(linha[1])

    soma += tabela[num] * qte

print("%.2f" % soma)