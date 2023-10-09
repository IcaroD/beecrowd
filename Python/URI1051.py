def entrada():
    enter = open("entrada.txt", "w")
    enter.write(input())
    enter.close()

def valor():
    valor = open("entrada.txt", "r")
    for linha in valor:
        a = float(linha)
    valor.close()
    return a

def saida(montande):
    if total > 0:
        saida = open("saida.txt", "w")
        saida.write("R$ %.2f"%montande)
        saida.close()
    else:
        saida = open("saida.txt", "w")
        saida.write("Isento")
        saida.close()

    saida = open("saida.txt", "r")
    for linha in saida:
        print(linha)
    saida.close()

enter = entrada()
a = valor()

total = 0
if(2000<a<=3000):
    t= (a-2000)
    tx= (t*8)/100
    total = tx
elif(3000<a<=4500):
    t= (a-2000)
    t1=t-1000
    tx1=(1000*8)/100
    tx2= (t1*18)/100
    total = tx1+tx2
else:
    t= (a-2000)
    t1= t-1000
    tx1= (1000*8)/100
    t2=t1-1500
    tx2=(1500*18)/100
    tx= (t2*28)/100
    total = tx+tx1+tx2
b = saida(total)