'''from math import factorial
num = int(input('insira um valor para calcular seu fatorial: '))
f = factorial(num)
print('o fatorial de {} é {}'.format(num,f))'''

num = int(input('insira um valor para calcular seu fatorial: '))
c = num
f = 1

print('fatorial de {}! = '.format(num),end='')
while c > 0: #fatorial termina em 1
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))