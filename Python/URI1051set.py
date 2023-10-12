imposto = [(2000, 8), (3000, 18), (4500, 28)]
montante = float(input())

juros = 0
for item in imposto:
    if montante > item[0]:
        valor = montante - item[0]
        if valor > 1000 and :
            juros += 1000 * item[1] / 100
        else:
            juros += valor * item[1] / 100

if juros == 0:
    print("Isento")
else:
    print("R$ %.2f" % juros)


