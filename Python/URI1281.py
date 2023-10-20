n = int(input())

for i in range(n):
    tabela = {}
    n1 = int(input())
    for j in range(n1):
        linha = input().split()
        chave = linha[0]
        preco = float(linha[1])
        tabela[linha[0]] = preco
    
    n2 = int(input())

    total = 0
    for j in range(n2):
        linha = input().split()
        chave = linha[0]
        qte = int(linha[1])
        total += tabela[chave] * qte
    
    print("R$ %.2f" % total)