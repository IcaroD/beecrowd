soma = 0
i = 0

while (i < 2):
    nota = float(input())

    if nota >= 0 and nota <= 10:
        soma += nota 
        i += 1
    else:
        print("nota invalida")

media = soma / 2

print("media = %.2f" % media)