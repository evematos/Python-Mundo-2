primeiro = int(input('insira primeiro termo: '))
razao = int(input('insira a razão da PA: '))
termo = primeiro
cont = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos você quer mostrar a mais?'))
print('progressão finalizada com {} termos exibidos'.format(total))
