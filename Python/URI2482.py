traducao = {}

n = int(input())

for i in range(n):
    chave = input()
    item = input()
    traducao[chave] = item

m = int(input())

for i in range(m*2):
    frase = input().split()
    for palavras in frase:
        if traducao.get(palavras) != None:
            print(traducao[palavras], end="")
        else:
            print(palavras, end="")
        
        if palavras != frase[len(frase)-1]:
            print(end=" ")
        else:
            print()
    if (i+1) % 2 == 0:
        print()