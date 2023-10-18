def entrada():
    enter = open("entrada.txt", "w")
    enter.write(input())
    enter.close()
    saida = open("entrada.txt", "r")
    linha = saida.readline()
    saida.close()

def saida():
    saida = open("saida.txt", "w")
    saida.write("Atraso maximo:", atraso)
    saida.close()

    saida = open("saida.txt", "r")
    saida.readline()
    saida.close()

while True:
    try:
        tempo = entrada()

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