def test(x, y, z, w):
    elements = [x, y, z, w]
    maior = max(elements)
    elements.remove(maior)
    maior_2 = max(elements)
    elements.remove(maior_2)

    if soma(elements) > maior_2 or (max(elements) + maior_2) > maior:
        return "S"
    else:
        return "N"

def soma(lista):
    result = 0
    for i in lista:
        result = result + i
    return result


values = input().split()
a = int(values[0])
b = int(values[1])
c = int(values[2])
d = int(values[3])

print(test(a, b, c, d))
