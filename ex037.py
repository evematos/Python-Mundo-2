num = int(input('insira um número inteiro: '))
print(' ')
print('''escolha uma das bases para conversão:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL''')
print(' ')
choice = int(input('Sua escolha: '))

if choice == 1:
    print('{} convertido em BINÁRIO é {}'.format(num,bin(num)[2:]))
elif choice == 2:
    print('{} convertido em OCTAL é {}'.format(num,oct(num)[2:]))
elif choice == 3:
    print('{} convertido em HEXADECIMAL é {}'.format(num,hex(num)[2:]))
else:
    print('Essa opção não existe. Tente novamente!!')

# [2:] fatiando a string para não aparecer a identificação das bases