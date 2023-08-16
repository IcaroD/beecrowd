value = input().split()
x = float(value[0])
y = float(value[1])
z = float(value[2])

a = max(x,y,z)
c = min(x,y,z)
b = min(max(x,y),max(x,z),max(y,z))
if a >= b + c:
    print("NAO FORMA TRIANGULO")

else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")

    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or c == a:
        print("TRIANGULO ISOSCELES")