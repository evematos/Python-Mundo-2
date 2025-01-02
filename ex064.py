num = int(input('digite um número para somar ou 999 para parar '))
soma = num

while num != 999:
    soma += num
    num = int(input('digite um número para somar ou 999 para parar '))
    print(soma)
print('FIM')
