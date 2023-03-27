from datetime import date

nasc = int(input('insira seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc

print('atleta: {} anos'.format(idade))

if idade <=9:
    print('categoria: MIRIM')
elif 9 < idade <= 14:
    print('categoria: INFANTIL')
elif 14 < idade <= 19:
    print('categoria: JÚNIOR')
elif 19 < idade <= 25:
    print('categoria: SÊNIOR')
elif idade > 25:
    print('categoria: MASTER')

