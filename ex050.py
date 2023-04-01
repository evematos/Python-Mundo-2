s = 0
cont = 0
for c in range(1,7):
    n = int(input('insira {} valor: '.format(c)))
    if n % 2 == 0:
        cont += 1
        s += n
print('você informou {} números pares e a soma deles é {}'.format(cont,s))