def verificacao(lista, qte):
    menor = int(lista[0])
    indice = 0
    for i in range(1, qte):
        if int(lista[i]) < menor:
            menor = int(lista[i])
            indice = i
    
    return menor, indice

N = int(input())
x = input().split()

menor, pos = verificacao(x, N)

print("Menor valor:", menor)
print("Posicao:", pos)