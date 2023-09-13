def calculo(peso, comp):
    return peso * comp

info = input().split()
p1 = int(info[0])
c1 = int(info[1])
p2 = int(info[2])
c2 = int(info[3])

result1 = calculo(p1, c1)
result2 = calculo(p2, c2)

if result1 == result2:
    resp = 0
elif result1 > result2:
    resp = -1
else:
    resp = 1

print(resp)