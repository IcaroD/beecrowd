tabela = {(1, 4.00), (2, 4.50), (3, 5.00), (4, 2.00), (5, 1.50)}

produto = input().split()
n = int(produto[0])
qte = int(produto[1])

for num in tabela:
    if num[0] == n:
        unid = num[1]
        
preco = unid * qte

print("Total: R$ %.2f" % preco)