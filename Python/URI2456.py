seq = input().split()

for i in range(len(seq)):
    seq[i] = int(seq[i])

ordem = sorted(seq)
invert = ordem[::-1]

if ordem == seq:
    resp = 'C'
elif invert == seq:
    resp = 'D'
else:
    resp = 'N'

print(resp)