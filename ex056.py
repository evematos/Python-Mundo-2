soma = 0
maiorid = 0
velho = ''
mulher = 0

for c in range(1,5):
    print('===== {}° pessoa ====='.format(c))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [F/M]: '))
    soma += idade

    if c == 1 and sexo in 'Mm':
        maiorid = idade
        velho = nome
    if sexo in 'Mm' and idade > maiorid:
        maiorid = idade
        velho = nome

    if sexo in 'Ff' and idade < 20:
        mulher += 1

print('='*18)
print('o grupo tem a idade média de {}'.format(soma/4))
print('o homem mais velho é {} com {} anos'.format(velho, maiorid))
print('existem no grupo {} mulheres com menos de 20 anos'.format(mulher))
