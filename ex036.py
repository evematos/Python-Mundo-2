from time import sleep

valor = float(input('insira valor da casa: '))
salario = float(input('insira salário do comprador: '))
ano = int(input('em quantos anos você vai pagar? '))

pres = valor / (ano * 12)
porc = (salario * 30) / 100

print('PROCESSANDO...')
sleep(1.5)

if pres > porc:
    print('Seu empréstimo foi NEGADO!!')
    print('Você não pode comprar a casa pois as parcelas são de R${:.2f}'.format(pres))
else:
    print('Parabéns!! Seu empréstimo foi aprovado com parcelas de R${:.2f}'.format(pres))