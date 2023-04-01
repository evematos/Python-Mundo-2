from datetime import date

menor = 0
maior = 0

for c in range(1,8):
    ano = int(input('{}° ano de nascimento: '.format(c)))
    idade = date.today().year - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1

print('='*25)
print('pessoas menores de idade: {}'.format(menor))
print('pessoas maiores de idade: {}'.format(maior))
print('='*25)
