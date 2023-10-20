n = int(input())

for i in range(n):
    traducao = {}

    numeros = input().split()
    qte = int(numeros[0])
    num = int(numeros[1])

    for j in range(qte):
        chave = input()
        resultado = input()
        traducao[chave] = resultado
    
    for j in range(num):
        frase = input().split()
        for item in frase:
            if traducao.get(item) == None:
                print(item, end="")
            else:
                print(traducao.get(item), end="")

            if frase[len(frase)-1] != item:
                print(end=" ")
        print()
    if i != n-1:
        print()
