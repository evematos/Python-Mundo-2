peso = float(input('insira seu peso em kg: '))
altura = float(input('insira sua altura em metros: '))

imc = peso / (altura * altura) # altura ** 2

print('seu IMC é de {:.1f}'.format(imc))
if imc < 16:
    print('classificação: MAGREZA GRAU III')
elif 16 <= imc <= 16.9:
    print('classificação: MAGREZA GRAU II')
elif 17 <= imc <=18.4:
    print('classificação: MAGREZA GRAU I')
elif 18.5 <= imc <= 24.9:
    print('classificação: ADEQUADO')
elif 25 <= imc <= 29.9:
    print('classificação: PRÉ-OBESO')
elif 30 <= imc <= 34.9:
    print('classificação: OBESIDADE GRAU I')
elif 35 <= imc <= 39.9:
    print('classificação: OBESIDADE GRAU II')
elif imc >= 40:
    print('classificação: OBESIDADE GRAU III')
