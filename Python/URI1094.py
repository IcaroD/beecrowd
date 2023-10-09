def porcentagem(total, tipo):
    temp = total / tipo
    return 100.0 / temp

N = int(input())

total = 0
C = 0
R = 0
S = 0
for i in range(N):
    cobaias = input().split()
    num = int(cobaias[0])
    total += num
    if cobaias[1] == "C":
        C += num
    if cobaias[1] == "R":
        R += num
    if cobaias[1] == "S":
        S += num

cp = porcentagem(total, C)
rp = porcentagem(total, R)
sp = porcentagem(total, S)

print("Total: %d cobaias" %total)
print("Total de coelhos:", C)
print("Total de ratos:", R)
print("Total de sapos:", S)
print("Percentual de coelhos: %.2f" %cp, "%")
print("Percentual de ratos: %.2f" %rp, "%")
print("Percentual de sapos: %.2f" %sp, "%")