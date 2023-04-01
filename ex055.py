maior = 0
menor = 0

for c in range(1,6):
    peso = float(input('{}° peso: kg'.format(c)))
    if c == 1: #se for o 1° sendo lido
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print('o maior peso foi {}kg'.format(maior))
print('o menor peso foi {}kg'.format(menor))