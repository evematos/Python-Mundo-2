print('='*10, 'LOJAS PONEI', '='*10)
valor = float(input('insira valor da compra: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
escolha = int(input('sua escolha: '))

if escolha == 1:
    total = valor - (valor * 10 / 100)
elif escolha == 2:
    total = valor - (valor * 5 / 100)
elif escolha == 3:
    total = valor
    parcela = total / 2
    print('sua compra será parcelada em 2X de R${:.2f} SEM JUROS'.format(parcela))
elif escolha == 4:
    div = int(input('total de parcelas: '))
    total = valor + (valor * 20 / 100)
    parcela = total / div
    print('sua compra será parcelada em {}X de R${:.2f} COM JUROS'.format(div,parcela))
else:
    total = valor #precisa estar definida para não dar erro
    print('opção inválida!! tente novamente')

print('sua compra de R${:.2f} sairá por R${:.2f}'.format(valor, total))
