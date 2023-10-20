falas = {"esquerda": "ingles", "direita": "frances", "nenhuma": "portugues", "as duas": "caiu"}

pernas = ""
while pernas != "as duas":
    pernas = input()
    print(falas[pernas])