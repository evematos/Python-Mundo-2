sexo = str(input('insira seu sexo [F/M] ')).strip().upper()[0] #somente a primeira letra

while sexo not in 'FM':
    sexo = str(input('inválido!!, insira seu sexo novamente [F/M] ')).upper()
print('-'*5)
print('dado registrado! sexo {}'.format(sexo))

