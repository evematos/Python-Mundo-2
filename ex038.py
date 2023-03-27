num1 = int(input('insira 1° número: '))
num2 = int(input('insira 2° número: '))

if num1 > num2:
    print('O primeiro valor é maior'.format(num1,num2))
elif num2 > num1:
    print('O seundo valor é maior'.format(num2,num1))
elif num1 == num2:
    print('Os valores são iguais'.format(num1,num2))
