from datetime import date

sex = int(input('''Como você se identifica: 
[ 1 ] mulher
[ 2 ] homem'''))
print('-=-'*13)

atual = date.today().year
nasc = int(input('insira seu ano de nascimento: '))
idade = atual - nasc

print('quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18 and sex == 2:
    print('você tem 18 anos e deve se alistar IMEDIATAMENTE!!')
elif idade > 18 and sex == 2:
    prazo = idade - 18
    ano = atual - prazo
    print('você deveria ter se alistado em {} há {} anos atrás'.format(ano, prazo))
elif idade < 18 and sex == 2:
    prazo = 18 - idade
    ano = atual + prazo
    print('você irá se alistar em {} daqui {} anos'.format(ano, prazo))
else:
    print('Parabéns!! Por ser mulher, você não precisa se alistar')


