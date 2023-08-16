value = int(input())

cem = value // 100
rest = value % 100
cinq = rest // 50
rest %= 50
vinte = rest // 20
rest %= 20
dez = rest // 10
rest %= 10
cinco = rest // 5
rest %= 5
dois = rest // 2
rest %= 2

print(value)
print(cem, "nota(s) de R$ 100,00")
print(cinq, "nota(s) de R$ 50,00")
print(vinte, "nota(s) de R$ 20,00")
print(dez, "nota(s) de R$ 10,00")
print(cinco, "nota(s) de R$ 5,00")
print(dois, "nota(s) de R$ 2,00")
print(rest, "nota(s) de R$ 1,00")