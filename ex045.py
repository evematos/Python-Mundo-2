from random import randint
from time import sleep
print('''suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

itens = ['pedra', 'papel', 'tesoura']
pc = randint(0,2)
jogador = int(input('escolha sua jogada: '))

sleep(0.4)
print('JO')
sleep(0.6)
print('KEN')
sleep(0.7)
print('PO!!')

print('-=-'*10)
print('computador jogou: {}'.format(itens[pc]))
print('jogador jogou: {}'.format(itens[jogador]))
print('-=-'*10)

if jogador == 0 or jogador == 1 or jogador == 2:
    if jogador == 0 and pc == 0 or jogador == 1 and pc == 1 or jogador == 2 and pc ==2:
        print('EMPATE')
    elif jogador == 0 and pc == 1 or jogador == 1 and pc == 2 or jogador == 2 and pc == 0:
        print('COMPUTADOR VENCE')
    elif pc == 0 and jogador == 1 or pc == 1 and jogador == 2 or pc == 2 and jogador == 0:
        print('JOGADOR VENCE')
else:
    print('jogada inválida, tente novamente!!')