while True:
    notas = set()
    qte = 0
    soma = 0
    while qte != 2:
        num = float(input())
        if num >= 0 and num <= 10:
            notas.add(num)
            qte += 1
        else:
            print("nota invalida")

    for i in notas:
        soma += i
        if len(notas) == 1:
            soma = i * 2

    media = soma / 2

    print("media = %.2f" % media)

    calculo = int(input("novo calculo (1-sim 2-nao)\n"))
    while calculo != 1:
        if calculo == 2:
            break
        calculo = int(input("novo calculo (1-sim 2-nao)\n"))

    if calculo == 2:
        break