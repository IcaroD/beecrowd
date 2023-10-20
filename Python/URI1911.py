n = int(input())

while n != 0:
    erros = 0
    assinatura = {}
    for i in range(2):
        for i in range(n):
            nome = input().split()

            if assinatura.get(nome[0]) == None:
                assinatura[nome[0]] = nome[1]
            else:
                if assinatura.get(nome[0]) != nome[1]:
                    erros = erros + 1

        n = int(input())
        if n == 0:
            break
    print(erros)