criptografia = {".": "a", "..": "b", "...": "c", ". .": "d", ".. ..": "e", "... ...": "f", ". . .": "g", ".. .. ..": "h", "... ... ...": "i", ". . . .": "j", ".. .. .. ..": "k", "... ... ... ...": "l", ". . . . .": "m", ".. .. .. .. ..": "n", "... ... ... ... ...": "o", ". . . . . .": "p", ".. .. .. .. .. ..": "q", "... ... ... ... ... ...": "r", ". . . . . . .": "s", ".. .. .. .. .. .. ..": "t", "... ... ... ... ... ... ...": "u", ". . . . . . . .": "v", ".. .. .. .. .. .. .. ..": "w", "... ... ... ... ... ... ... ...": "x", ". . . . . . . . .": "y", ".. .. .. .. .. .. .. .. ..": "z"}

while True:
    try:
        n = int(input())
        for j in range(n):
            pontos = input()
            print(criptografia[pontos])
    except EOFError:
        break