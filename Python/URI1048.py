salario = float(input())

percentual = 0
if salario <= 400:
    percentual = 15
elif salario <= 800:
    percentual = 12
elif salario <= 1200:
    percentual = 10
elif salario <= 2000:
    percentual = 7
else:
    percentual = 4

adicional = salario * percentual / 100
salario += adicional

print("Novo salario: %.2f" %salario)
print("Reajuste ganho: %.2f" %adicional)
print("Em percentual:", percentual, "%")