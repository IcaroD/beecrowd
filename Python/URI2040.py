n = int(input())

while n != 0:
    campeonato = {}
    for i in range(n):
        linha = input().split()
        s = linha[0]
        p = int(linha[1])
        campeonato[s] = p
    
    for i in range(n//2):
        linha = input().split()
        timeA = linha[0]
        timeB = linha[2]
        gols = linha[1].split("-")
        golA = int(gols[0])
        golB = int(gols[1])

        campeonato[timeA] += golA * 3
        campeonato[timeB] += golB * 3

        if golA > golB:
            campeonato[timeA] += 5
        elif golA == golB:
            campeonato[timeA] += 1
            campeonato[timeB] += 1
        else:
            campeonato[timeB] += 5
    
    venceu = True
    vencedor = "Sport"
    for item in campeonato:
        if campeonato[item] > campeonato[vencedor]:
            venceu = False
            vencedor = item 
    
    if venceu == True:
        print("O %s foi o campeao com %d pontos :D" % (vencedor, campeonato[vencedor]))
    else:
        print("O Sport nao foi o campeao. O time campeao foi o %s com %d pontos :(" % (vencedor, campeonato[vencedor]))
    print()
    
    n = int(input())