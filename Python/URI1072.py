qte = int(input())

n = []

for i in range(0, qte):
    x = int(input())
    n.append(x)

dentro = 0
fora = 0
for i in range(0, qte):
    if n[i] >= 10 and n[i] <= 20:
        dentro += 1
    else:
        fora += 1

print(dentro, "in")
print(fora, "out")