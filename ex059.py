v1 = int(input('primeiro valor: '))
v2 = int(input('segundo valor: '))
opcao = 0

while opcao != 5:
    print('-=-'*15)
    print('qual operação você deseja realizar?')
    print('[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior valor \n[ 4 ] novos números \n[ 5 ] sair do programa')
    opcao = int(input('>>>>>> escolha uma operação: '))
    if opcao <= 5:
        if opcao == 1:
            soma = v1 + v2
            print('a soma é {} + {} = {}'.format(v1,v2,soma))
        elif opcao == 2:
            mult = v1 * v2
            print('a multiplicação é {} x {} = {}'.format(v1, v2, mult))
        elif opcao == 3:
            if v1 > v2:
                maior = v1
                print('o maior número entre {} e {} é {}'.format(v1, v2, maior))
            elif v2 > v1:
                maior = v2
                print('o maior número entre {} e {} é {}'.format(v1, v2, maior))
            else:
                print('{} e {} são iguais'.format(v1,v2))
        elif opcao == 4:
            print('insira os novos números')
            v1 = int(input('primeiro valor: '))
            v2 = int(input('segundo valor: '))
    else:
        print('Opção inválida, tente novamente!')
print('Obrigada, volte sempre!')
