values = input().split()
ihour = int(values[0])
imin = int(values[1])
fhour = int(values[2])
fmin = int(values[3])

hour = fhour - ihour 
minute = fmin - imin

if minute < 0:
    minute += 60
    hour -= 1

if imin == fmin and ihour == fhour:
    hour = 24
elif hour < 0 and imin > fmin:
    hour += 24

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hour, minute))