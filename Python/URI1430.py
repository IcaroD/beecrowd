duracao = {"W": 1, "H": 0.5, "Q": 0.25, "E": 0.125, "S": 0.0625, "T": 0.03125, "X": 0.015625}
jingle = input()

while jingle != "*":
    compasso = jingle.split("/")
    compasso.pop(-1)
    compasso.pop(0)
    acerto = 0
    for item in compasso:
        tempo = 0
        for letras in item:
            tempo += duracao[letras]
        if tempo == 1:
            acerto += 1
    print(acerto)
    jingle = input()