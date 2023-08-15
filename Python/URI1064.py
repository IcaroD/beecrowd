num = []

for i in range(0,6):
    numero = float(input())
    num.append(numero)

soma = 0
positivo = 0
for i in range(0,6):
    if num[i] > 0:
        soma += num[i]
        positivo += 1

media = soma / positivo

print(positivo, "valores positivos")
print("%.1f" % media)