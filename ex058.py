from random import randint

print('estou pensando em um número entre 0 e 10')
print('tente a sorte, consegue adivinhar?')
numpc = randint(0,10)
numus = int(input('qual é o seu palpite?'))

tentativas = 1
while numus != numpc:
    if numpc > numus:
        print('o número que estou pensando é MAIOR')
    else:
        print('o número que estou pensando é MENOR')
    numus = int(input('qual é o seu palpite?'))
    tentativas += 1
print('PARABÉNS! você acertou com {} tentativas'.format(tentativas))
