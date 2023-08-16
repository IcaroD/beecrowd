values = input().split()
x = float(values[0])
y = float(values[1])
z = float(values[2])

a = max(x,y,z)
b = min(max(x,y),max(x,z),max(y,z))
c = min(x,y,z)

if a < b + c:
    perimetro = a + b + c
    print("Perimetro = %.1f" % perimetro)
else:
    area = (a + b) * c / 2.0
    print("Area = %.1f" % area)