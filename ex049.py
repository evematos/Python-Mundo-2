n = int(input('insira um número inteiro: '))
print('='*10,'tabuada de {}'.format(n), '='*10)

for c in range(0,11):
    print('{} x {} = {}'.format(n, c, (n*c)))