N = int(input())
c = []
l = []

for i in range(N):
    bandeja = input().split()
    l.append(int(bandeja[0]))
    c.append(int(bandeja[1]))

queda = 0
for i in range(N):
    if l[i] > c[i]:
        queda += c[i]

print(queda)