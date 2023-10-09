while True:
    try:
        tempo = input().split(":")

        tempo[0] = int(tempo[0]) + 1
        atraso = 0
        if tempo[0] == 8:
            atraso = int(tempo[1])
        if tempo[0] >= 9:
            horas = tempo[0] - 8
            atraso = int(tempo[1]) + horas * 60

        print("Atraso maximo:", atraso)
    except EOFError:
        break