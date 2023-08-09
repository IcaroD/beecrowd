nome = input()
fixo = float(input())
montante = float(input())

bonus = montante * 15 / 100
salario = fixo + bonus

print("TOTAL = R$ %.2f" %(salario))