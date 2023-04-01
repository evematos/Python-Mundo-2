i = int(input('insira primeiro termo: '))
p = int(input('insira a razão da PA: '))
d = i + (10-1) * p

for c in range(i, d + p, p):
    print(c, end=' -> ')
print('FIM')