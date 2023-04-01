n = int(input('insira um número inteiro: '))
total = 0

for c in range(1,n+1):
    if n % c == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')

    print('{} '.format(c), end='')

print('\n\033[mo número {} é divisível por {} números'.format(n,total))
if total == 2:
    print('por isso É PRIMO')
else:
    print('por isso NÃO É PRIMO')